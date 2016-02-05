from collections import namedtuple
from enum import Enum
from math import floor, log10
from sys import stdout

Result = namedtuple('Result', 'id caller status message')
Status = Enum('Status', 'Ok, Fail')


def makeResult(id, caller, status, message=""):
    result = None
    if(id >= 0 and caller is not None and status is not None and message is not None):
        if message != "":
            message = "-> {0}".format(message)
        result = Result(id, "[{0}]".format(caller), status, message)
    return result


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
        self.tests = [method for method in dir(self)
                      if callable(getattr(self, method)) and method.startswith("test")]

    def run(self):
        # Reset the id counter.
        self.id = 0

        finishedTests = []
        for test in self.tests:
            func = getattr(self, test, None)

            # Run the setup method.
            self.setup()
            # Run the test method.
            func()
            # Run the teardown method.
            self.teardown()

            # Add the test to the finishedTests list and increment the id
            # counter.
            finishedTests.append((self.id, test))
            self.id = self.id + 1

        self.__printResults(finishedTests)

    def __printResults(self, tests):
        if tests is not None:
            print("Case -> {0}".format(self.name))

            size = len(tests)

            idLength = int(floor(log10(size)))
            nameLength = max([len(test[1]) for test in tests])
            statusLength = 12   # Status.Fail is longest output
            callerLength = max([len(result.caller) for result in self.results])
            messageLength = max([len(result.message)
                                 for result in self.results])

            for i in range(0, idLength + 3 + nameLength + 2 + statusLength + 1 + callerLength + 1 + messageLength):
                print("-", end="")
            print("")

            for i in range(0, self.id):
                # Get all results for that test with id i.
                results = [result for result in self.results if result.id == i]
                for result in results:
                    print("[{0:<{idLength}}] {1:<{nameLength}}: {2:<{statusLength}}|{4:>{callerLength}} {3}".format(
                        i, [test[1]for test in tests if i == test[0]][0],
                        result.status, result.message, result.caller, idLength=idLength,
                        nameLength=nameLength, statusLength=statusLength, callerLength=callerLength))

            for i in range(0, idLength + 3 + nameLength + 2 + statusLength + 1 + callerLength + 1 + messageLength):
                print("-", end="")
            print("")

    def setup(self):
        """The setup method is executed before every single test.
        """
        pass

    def teardown(self):
        """The teardown method is executed after every single test.
        """
        pass

    def __assertEqual(self, value, expected, caller):
        if value == expected:
            result = makeResult(self.id, caller, Status.Ok)
        else:
            result = makeResult(
                self.id, caller, Status.Fail, "{0} is not equal to {1}".format(value, expected))
        self.results.append(result)

    def assertEqual(self, value, expected):
        """Checks whether value is equal to expected.

            Args:
                value (object): The value to be tested.
                expected (object): The value to be compared to.
        """
        self.__assertEqual(value, expected, "assertEqual")

    def assertNotEqual(self, value, expected):
        """Checks whether value is not equal to expected.

            Args:
                value (object): The value to be checked.
                expected (object): The value to be compared to.
        """
        if value != expected:
            result = makeResult(self.id, "assertNotEqual", Status.Ok)
        else:
            result = makeResult(
                self.id, "assertNotEqual", Status.Fail, "{0} is equal to {1}".format(value, expected))
        self.results.append(result)

    def assertTrue(self, value):
        """Checks whether value is to boolean value True.

            Args:
                value (boolean): The value to be checked.
        """
        self.__assertEqual(value, True, "assertTrue")

    def assertFalse(self, value):
        """Checks whether value is the boolean value False.

            Args:
                value (boolean): The value to be checked.
        """
        self.__assertEqual(value, False, "assertFalse")

    def __assertIs(self, value, expected, caller):
        if value is expected:
            result = makeResult(self.id, caller, Status.Ok)
        else:
            result = makeResult(
                self.id, caller, Status.Fail, "{0} is not {1}".format(value, expected))
            self.results.append(result)

    def assertIs(self, value, expected):
        """Check whether value is expected.

            Args:
                value (object): The value to be checked.
                expected (object): The value to be compared to.
        """
        self.__assertIs(value, expected, "assertIs")

    def __assertIsNot(self, value, expected, caller):
        if value is expected:
            result = makeResult(self.id, caller, Status.Ok)
        else:
            result = makeResult(
                self.id, caller, Status.Fail, "{0} is {1}".format(value, expected))
        self.results.append(result)

    def assertIsNot(self, value, expected):
        """Check whether the value is not expected.

            Args:
                value (object): The value to be checked.
                expected (object): The value to be compared to.
        """
        self.__assertIsNot(value, expected, "assertIsNot")

    def assertIsNone(self, value):
        """Checks whether value is None.

            Args:
                value (object): The value to be checked.
        """
        self.__assertIs(value, None, "assertIsNone")

    def assertIsNotNone(self, value):
        """Checks whether the value is not None.

            Args:
                value (object): The value to be checked.
        """
        self.__assertIsNot(value, None, "assertIsNotNone")

    def assertIn(self, value, collection):
        """Checks whether value is in the collection.

            Args:
                value (object): The value to be checked.
                collection (object): The collection the object should be in.
        """
        if value in collection:
            result = makeResult(self.id, "assertIn", Status.Ok)
        else:
            result = makeResult(self.id, "assertIn", Status.Fail,
                                "{0} is not in {1}".format(value, collection))
        self.results.append(result)

    def assertNotIn(self, value, collection):
        """Checks whether value is not in the collection.

            Args:
                value (object): The value to be checked.
                collection (object): The collection the object should not be in.
        """
        if value not in collection:
            result = makeResult(self.id, "assertNotIn", Status.Ok)
        else:
            result = makeResult(self.id, "assertNotIn", Status.Fail,
                                "{0} is in {1}".format(value, collection))
        self.results.append(result)

    def assertRaises(self, exception, func, *args, **kwargs):
        """Checks whether the function 'func' raises an expection of type 'exception'.

            Args:
                exception (class(Exception)): The type of the exception to watch out for.
                func (function): The function to execute.
                *args (args): The arguments for the function.
        """
        try:
            func(*args, **kwargs)
            result = makeResult(self.id, "assertRaises", Status.Fail, "{0} did not throw {1}".format(
                func.__name__, exception.__name__))
        except exception as e:
            result = makeResult(self.id, "assertRaises", Status.Ok)
        self.results.append(result)
