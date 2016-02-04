from collections import namedtuple
from enum import Enum
from sys import stdout

Result = namedtuple('Result', 'id status message')
Status = Enum('Status', 'Ok, Fail, Error')


class Suite:
    """A Suite is a group of cases, that are executed sequentially.

        Attributes:
            name (str): The name of the suite.
            cases ([Case]): The cases that belong to this suite.
    """

    def __init__(self, name):
        """Creates an empty Suite with the given name.

            Args:
                name (str): The name of the suite.
        """
        self.name = name
        self.cases = []

    def add(self, case):
        """Adds a case to the suite.

            Args:
                case (Case): The case that will be added.
        """
        if case is not None and isinstance(case, Case):
            self.cases.append(case)

    def run(self, out=stdout, verbose=True):
        """Runs all cases the suite has sequentially and prints them to the output.

            Args:
                out (Optional(file)): The output the suite will print to, default is stdout.
                verbose (Optional(boolean)): Whether the output should be verbose, defaults to True.
        """
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

                    case.setup()
                    func()
                    case.teardown()

                    case.id = case.id + 1
            except FailError as e:
                # If we hit a FailError, stop execution and skip to the next
                # case.
                pass

        # Print everything to the output.
        print("Suite: {0}".format(self.name), file=out)
        print("***************************************************************")
        for case in self.cases:
            self.__printCase(out, case, verbose)
        print("***************************************************************")

    def __printCase(self, out, case, verbose):
        """Prints a case to the output.

            Args:
                out (file): The output the method prints to.
                case (Case): The case that will be printed.
                verbose (boolean): Whether the output should be verbose.
        """
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
    """A case has multiple tests, that are executed when the suite it belongs to, is run.

        Attributes:
            id (int): A incrementing id, that increases for every test.
            name (str): The name of the test-case.
            results ([Result]): Results for every assertion in this case.
            tests ([(int, str)]): A list of tuples containing the id of a test and its name.
    """

    def __init__(self, name):
        """Creates a case with the given name.

            Args:
                name (str): The name of the case.
        """
        self.name = name
        self.id = 0
        self.results = []
        self.tests = []

    def setup(self):
        """The setup method is executed before every single test.
        """
        pass

    def teardown(self):
        """The teardown method is executed after every single test.
        """
        pass

    def assertEqual(self, value, expected):
        """Checks whether value is equal to expected.

            Args:
                value (object): The value to be tested.
                expected (object): The value to be compared to.
        """
        if value == expected:
            self.results.append(Result(self.id, Status.Ok, ""))
        else:
            self.results.append(Result(self.id, Status.Fail,
                                       "{0} is not {1}".format(value, expected)))

    def assertNotEqual(self, value, expected):
        """Checks whether value is not equal to expected.

            Args:
                value (object): The value to be checked.
                expected (object): The value to be compared to.
        """
        if value != expected:
            self.results.append(Result(self.id, Status.Ok, ""))
        else:
            self.results.append(Result(self.id, Status.Fail,
                                       "{0} is not {1}".format(value, expected)))

    def assertTrue(self, value):
        """Checks whether value is to boolean value True.

            Args:
                value (boolean): The value to be checked.
        """
        self.assertEqual(value, True)

    def assertFalse(self, value):
        """Checks whether value is the boolean value False.

            Args:
                value (boolean): The value to be checked.
        """
        self.assertEqual(value, False)

    def assertIs(self, value, expected):
        """Check whether value is expected.

            Args:
                value (object): The value to be checked.
                expected (object): The value to be compared to.
        """
        if value is expected:
            self.results.append(Result(self.id, Status.Ok, ""))
        else:
            self.results.append(Result(self.id, Status.Fail,
                                       "{0} is not {1}".format(value, expected)))

    def assertIsNot(self, value, expected):
        """Check whether the value is not expected.

            Args:
                value (object): The value to be checked.
                expected (object): The value to be compared to.
        """
        if value is not expected:
            self.results.append(Result(self.id, Status.Ok, ""))
        else:
            self.results.append(Result(self.id, Status.Fail,
                                       "{0} is {1}".format(value, expected)))

    def assertIsNone(self, value):
        """Checks whether value is None.

            Args:
                value (object): The value to be checked.
        """
        self.assertIs(value, None)

    def assertIsNotNone(self, value):
        """Checks whether the value is not None.

            Args:
                value (object): The value to be checked.
        """
        self.assertIsNot(value, None)

    def assertIn(self, value, collection):
        """Checks whether value is in the collection.

            Args:
                value (object): The value to be checked.
                collection (object): The collection the object should be in.
        """
        if value in collection:
            self.results.append(Result(self.id, Status.Ok, ""))
        else:
            self.results.append(
                Result(self.id, Status.Fail, "{0} is not in {1}".format(value, collection)))

    def assertNotIn(self, value, collection):
        """Checks whether value is not in the collection.

            Args:
                value (object): The value to be checked.
                collection (object): The collection the object should not be in.
        """
        if value not in collection:
            self.results.append(Result(self.id, Status.Ok, ""))
        else:
            self.results.append(
                Result(self.id, Status.Fail, "{0} is in {1}".format(value, collection)))

    def assertRaises(self, exception, func, *args, **kwargs):
        """Checks whether the function 'func' raises an expection of type 'exception'.

            Args:
                exception (class(Exception)): The type of the exception to watch out for.
                func (function): The function to execute.
                *args (args): The arguments for the function.
        """
        try:
            func(*args, **kwargs)
            self.results.append(Result(
                self.id, Status.Fail, "{0} did not throw {1}".format(func.__name__, exception.__name__)))
        except exception as e:
            self.results.append(Result(self.id, Status.Ok, ""))

    def failUnless(self, value, expected):
        """Fails the case, if value is not equal to expected.

            Args:
                value (object): The value to be checked.
                expected (object): The value to be compared to.
        """
        if value == expected:
            self.results.append(Result(self.id, Status.Ok, ""))
        else:
            self.results.append(
                Result(self.id, Status.Error, "{0} is not {1} | Execution stopped.".format(value, expected)))
            raise FailError("")


class FailError(Exception):
    """An exception that shows a failure condition was met.

        Attributes:
            message (str): A user-defined message.
    """

    def __init__(self, message):
        """Creates an exception with a user-defined message.

            Args:
                message (str): The message.
        """
        self.message = message

    def __str__(self):
        """Returns the message.
        """
        return self.message
