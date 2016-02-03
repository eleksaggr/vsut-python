from collections import namedtuple
from enum import Enum
from sys import stdout

Result = namedtuple('Result', 'id status message')
Status = Enum('Status', 'Ok, Fail, Error')


class Suite:

    def __init__(self, name):
        self.name = name
        self.cases = []

    def add(self, case):
        if case is not None and isinstance(case, Case):
            self.cases.append(case)

    def run(self, out=stdout, verbose=True):
        # Execute all cases.
        for case in self.cases:
            try:
                # Run all methods of the case that start with 'test'.
                tests = [method for method in dir(case)
                         if callable(getattr(case, method)) and method.startswith("test")]
                for test in tests:
                    func = getattr(case, test, None)

                    # Add the name of the test to the case, together with its
                    # id.
                    case.tests.append((case.id, test))

                    func()
                    case.id = case.id + 1
            except FailError as e:
                # If we hit a FailError, stop execution and skip to the next
                # case.
                pass

        # Print everything to the output.
        print("Suite: {0}".format(self.name), file=out)
        print("***************************************************************")
        for case in self.cases:
            self.__printCase(case, verbose)
        print("***************************************************************")

    def __printCase(self, case, verbose):
        print("Case: {0}".format(case.name))

        for test in case.tests:
            id = test[0]
            name = test[1]

            # Check if the test passed all its conditions.
            statuses = [
                result.status for result in case.results if result.id == id]
            status = Status.Ok
            for s in statuses:
                if s != Status.Ok:
                    status = s
                    break

            if verbose:
                for result in case.results:
                    if result.id == id:
                        # Add parentheses to the message.
                        message = ""
                        if result.message is not None and result.message != "":
                            message = "...({0})".format(result.message)

                        # Convert status enum to string.
                        if result.status == Status.Ok:
                            status = "Ok"
                        elif result.status == Status.Fail:
                            status = "Fail"
                        else:
                            status = "Error"

                        print("  [{0}]{1}:\t{2}{3}".format(
                            id, name, status, message), file=out)
            else:
                if status == Status.Ok:
                    print("  [{0}]{1}:\t{2}".format(
                        id, name, "Ok"), file=out)
                elif status == Status.Fail:
                    print("  [{0}]{1}:\t{2}".format(
                        id, name, "Fail"), file=out)
                else:
                    print("  [{0}]{1}:\t{2}".format(
                        id, name, "Error"), file=out)


class Case:

    def __init__(self, name):
        self.name = name
        self.id = 0
        self.results = []
        self.tests = []

    def assertEqual(self, value, expected):
        if value == expected:
            self.results.append(Result(self.id, Status.Ok, ""))
        else:
            self.results.append(Result(self.id, Status.Fail,
                                       "{0} is not {1}".format(value, expected)))

    def assertNotEqual(self, value, expected):
        if value != expected:
            self.results.append(Result(self.id, Status.Ok, ""))
        else:
            self.results.append(Result(self.id, Status.Fail,
                                       "{0} is not {1}".format(value, expected)))

    def assertTrue(self, value):
        self.assertEqual(value, True)

    def assertFalse(self, value):
        self.assertEqual(value, False)

    def assertIs(self, value, expected):
        if value is expected:
            self.results.append(Result(self.id, Status.Ok, ""))
        else:
            self.results.append(Result(self.id, Status.Fail,
                                       "{0} is not {1}".format(value, expected)))

    def assertIsNot(self, value, expected):
        if value is not expected:
            self.results.append(Result(self.id, Status.Ok, ""))
        else:
            self.results.append(Result(self.id, Status.Fail,
                                       "{0} is {1}".format(value, expected)))

    def assertIsNone(self, value):
        self.assertIs(value, None)

    def assertIsNotNone(self, value):
        self.assertIsNot(value, None)

    def assertIn(self, value, collection):
        if value in collection:
            self.results.append(Result(self.id, Status.Ok, ""))
        else:
            self.results.append(
                Result(self.id, Status.Fail, "{0} is not in {1}".format(value, collection)))

    def assertNotIn(self, value, collection):
        if value not in collection:
            self.results.append(Result(self.id, Status.Ok, ""))
        else:
            self.results.append(
                Result(self.id, Status.Fail, "{0} is in {1}".format(value, collection)))

    def assertRaises(self, exception, func, *args, **kwargs):
        try:
            func(*args, **kwargs)
            self.results.append(Result(
                self.id, Status.Fail, "{0} did not throw {1}".format(func.__name__, exception.__name__)))
        except exception as e:
            self.results.append(Result(self.id, Status.Ok, ""))

    def failUnless(self, value, expected):
        if value == expected:
            self.results.append(Result(self.id, Status.Ok, ""))
        else:
            self.results.append(
                Result(self.id, Status.Error, "{0} is not {1} | Execution stopped.".format(value, expected)))
            raise FailError("")


class FailError(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
