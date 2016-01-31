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

    def run(self, out=stdout, verbose=False):
        id = 0
        for case in self.cases:
            try:
                # TODO: Run all methods of the case that start with 'test'.
                print(case.tests)
                for test in case.tests:
                    func = getattr(case, test, None)
                    func()
            except FailError as e:
                # If we hit a FailError, stop execution and skip to the next
                # case.
                pass
            id = id + 1

        print("Suite: {0}".format(self.name), file=out)
        print("***************************************************************")
        print("\t--------------------------------------------------")
        for case in self.cases:
            success = True

            print("\tCase: {0}".format(case.name), file=out)
            for result in case.results:
                # Convert enum status to string representation.
                if result.status == Status.Ok:
                    status = "OK"
                elif result.status == Status.Fail:
                    status = "FAIL"
                    success = False
                else:
                    status = "ERROR"
                    success = False
                if verbose:
                    # If there is a message, add parentheses to it.
                    if result.message is not None and result.message is not "":
                        result = Result(result.id, result.status,
                                        "({0})".format(result.message))

                    print("\t\t{0}:\t {2} {1}".format(
                        result.id, result.message, status), file=out)
                    print("\t----------------------------------------------------")
            if not verbose:
                print("\t\tSuccess: {0}".format(success))
                print("\t----------------------------------------------------")
        print("***************************************************************")


def test(func):
    def func_wrapper(self):
        if func.__name__ not in self.tests:
            self.tests.append(func.__name__)
    return func_wrapper


class Case:

    def __init__(self, name):
        self.name = name
        self.id = 0
        self.results = []
        self.tests = []

    def run(self, method):
        self.method()

    def assertEqual(self, value, expected):
        if value == expected:
            self.results.append(Result(self.id, Status.Ok, ""))
        else:
            self.results.append(Result(self.id, Status.Fail,
                                       "{0} is not {1}".format(value, expected)))
        self.id = self.id + 1

    def assertNotEqual(self, value, expected):
        if value != expected:
            self.results.append(Result(self.id, Status.Ok, ""))
        else:
            self.results.append(Result(self.id, Status.Fail,
                                       "{0} is not {1}".format(value, expected)))
        self.id = self.id + 1

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
        self.id = self.id + 1

    def assertIsNot(self, value, expected):
        if value is not expected:
            self.results.append(Result(self.id, Status.Ok, ""))
        else:
            self.results.append(Result(self.id, Status.Fail,
                                       "{0} is {1}".format(value, expected)))
        self.id = self.id + 1

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
        self.id = self.id + 1

    def assertNotIn(self, value, collection):
        if value not in collection:
            self.results.append(Result(self.id, Status.Ok, ""))
        else:
            self.results.append(
                Result(self.id, Status.Fail, "{0} is in {1}".format(value, collection)))
        self.id = self.id + 1

    def assertRaises(self, exception, func, *args, **kwargs):
        try:
            func(*args, **kwargs)
            self.results.append(Result(
                self.id, Status.Fail, "{0} did not throw {1}".format(func.__name__, exception)))
        except exception as e:
            self.results.append(Result(self.id, Status.Ok, ""))
        self.id = self.id + 1

    def failUnless(self, value, expected):
        if value == expected:
            self.results.append(Result(self.id, Status.Ok, ""))
        else:
            self.results.append(
                Result(self.id, Status.Error, "{0} is not {1} | Execution stopped.".format(value, expected)))
            raise FailError("")
        self.id = self.id + 1


class FailError(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
