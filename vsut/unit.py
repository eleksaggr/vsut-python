from collections import namedtuple
from enum import Enum
from math import floor, log10
from sys import stdout
from vsut.assertion import AssertException

AssertionFail = namedtuple("Fail", "id, exception")


class Unit():
    """A unit is a group of tests, that are run at once.

    Every method of this class, that starts with 'test' will be run automatically,
    when the run()-method is called.
    Before and after every test the setup and teardown methods will be called respectively.

        Attributes:
            tests ([(int, str)]): A list of tests for this unit.
            failedAssertions ([AssertionFail]): Failed assertions in this unit.
    """

    def __init__(self):
        self.tests = [(id, funcName) for id, funcName in enumerate([method for method in dir(self)
                                                                    if callable(getattr(self, method)) and method.startswith("test")])]
        self.failedAssertions = []

    def run(self):
        """Runs all tests in this unit.
        """
        for id, test in self.tests:
            try:
                # Get the method that needs to be executed.
                func = getattr(self, test, None)

                # Run the setup method.
                self.setup()
                # Run the test method.
                func()
                # Run the teardown method.
                self.teardown()
            except AssertException as e:
                self.failedAssertions.append(AssertionFail(id, e))

    def setup(self):
        """Setup is executed before every test.
        """
        pass

    def teardown(self):
        """Teardown is executed after every test.
        """
        pass


class Formatter():
    """A Formatter formats the results of a unit for viewing.
    """

    def __init__(self, unit):
        self.unit = unit

    def format(self):
        """Formats the result of a unit.
        """
        pass

    def __str__(self):
        return self.format()


class TableFormatter(Formatter):
    """A TableFormatter formats the results of a unit as a table.

    The table looks as follows:
    [Id] Testname -> Status (| [Assertion] -> Message)
    """

    def format(self):
        ret = "Case -> {0}\n".format(type(self.unit).__name__)

        idLength = int(floor(log10(len(self.unit.tests)))) + 3
        nameLength = max([len(test[1]) for test in self.unit.tests])

        if len(self.unit.failedAssertions) != 0:
            assertLength = max(
                [len(fail.exception.assertion.__name__) for fail in self.unit.failedAssertions]) + 2
        else:
            assertLength = 0

        for id, test in self.unit.tests:
            fails = [
                fail.exception for fail in self.unit.failedAssertions if fail.id == id]
            if len(fails) == 0:
                ret += "\t{0:>{idLength}} {1:<{nameLength}} -> Ok\n".format(
                    "[{0}]".format(id), test, idLength=idLength, nameLength=nameLength)
            else:
                for fail in fails:
                    message = fail.message
                    if message is not None and message != "":
                        message = "-> {0}".format(fail.message)
                    ret += "\t{0:>{idLength}} {1:<{nameLength}} -> Fail | {2:<{assertLength}} {3}\n".format("[{0}]".format(id), test, "[{0}]".format(
                        fail.assertion.__name__), message, idLength=idLength, nameLength=nameLength, assertLength=assertLength)
        return ret


class CSVFormatter(Formatter):
    """
    """

    def format(self, separator=","):
        ret = "{0}\n".format(type(self.unit).__name__)

        for id, test in self.unit.tests:
            fails = [
                fail.exception for fail in self.unit.failedAssertions if fail.id == id]
            if len(fails) == 0:
                ret += "{1}{0}{2}{0}Ok\n".format(separator, id, test)
            else:
                for fail in fails:
                    ret += "{1}{0}{2}{0}Fail{0}{3}{0}{4}\n".format(
                        separator, id, test, fail.assertion.__name__, fail.message)
        return ret
