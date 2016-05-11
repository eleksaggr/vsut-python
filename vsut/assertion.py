"""Assertions for testing of conditions.

This module contains assertions that can be used in unit testing.
"""


def assertEqual(expected, actual, message=""):
    """Checks whether expected is equal to actual.

        Args:
            expected (object): The expected object.
            actual (object): The actual object.
            message (Optional[str]): An optional error message,
                that is displayed if the assertion fails.

        Raises:
            AssertResult: If an assertion fails.
    """
    if expected != actual:
        if message == "":
            message = "{0} != {1}".format(expected, actual)
        raise AssertResult(assertEqual.__name__, message)


def assertNotEqual(expected, actual, message=""):
    """Checks whether expected is not equal to actual.

        Args:
            expected (object): The expected object.
            actual (object): The actual object.
            message (Optional[str]): An optional error message,
                that is displayed if the assertion fails.

        Raises:
            AssertResult: If an assertion fails.
    """
    if expected == actual:
        if message == "":
            message = "{0} == {1}".format(expected, actual)
        raise AssertResult(assertNotEqual.__name__, message)


def assertTrue(expected, message=""):
    """Checks whether expected is equal to True.

        Args:
            expected (object): The expected object.
            message (Optional[str]): An optional error message,
                that is displayed if the assertion fails.

            Raises:
                AssertResult: If an assertion fails.
    """
    if expected != True:
        if message == "":
            message = "{0} != True".format(expected)
        raise AssertResult(assertTrue.__name__, message)


def assertFalse(expected, message=""):
    """Checks whether expected is equal to False.

        Args:
            expected (object): The expected object.
            message (Optional[str]): An optional error message,
                that is displayed if the assertion fails.

        Raises:
            AssertResult: If an assertion fails.
    """
    if expected != False:
        if message == "":
            message = "{0} != False".format(expected)
        raise AssertResult(assertFalse.__name__, message)


def assertIs(expected, actual, message=""):
    """Checks whether expected is actual.

        Args:
            expected (object): The expected object.
            actual (object): The actual object.
            message (Optional[str]): An optional error message,
                that is displayed if the assertion fails.

        Raises:
            AssertResult: If an assertion fails.
    """
    if expected is not actual:
        if message == "":
            message = "{0} is not {1}".format(expected, actual)
        raise AssertResult(assertIs.__name__, message)


def assertIsNot(expected, actual, message=""):
    """Checks whether expected is not actual.

        Args:
            expected (object): The expected object.
            actual (object): The actual object.
            message (Optional[str]): An optional error message,
                that is displayed if the assertion fails.

        Raises:
            AssertResult: If an assertion fails.
    """
    if expected is actual:
        if message == "":
            message = "{0} is {1}".format(expected, actual)
        raise AssertResult(assertIsNot.__name__, message)


def assertIsNone(expected, message=""):
    """Checks whether expected is None.

        Args:
            expected (object): The expected object.
            message (Optional[str]): An optional error message,
                that is displayed if the assertion fails.

        Raises:
            AssertResult: If an assertion fails.
    """
    if expected != None:
        if message == "":
            message = "{0} is not None".format(expected)
        raise AssertResult(assertIsNone.__name__, message)


def assertIsNotNone(expected, message=""):
    """Checks whether expected is not None.

        Args:
            expected (object): The expected object.
            message (Optional[str]): An optional error message,
                that is displayed if the assertion fails.

        Raises:
            AssertResult: If an assertion fails.
    """
    if expected == None:
        if message == "":
            message = "{0} is None".format(expected)
        raise AssertResult(assertIsNotNone.__name__, message)


def assertIn(expected, collection, message=""):
    """Checks whether expected is in collection.

        Args:
            expected (object): The expected object.
            collection (object): The collection to check in.
            message (Optional[str]): An optional error message,
                that is displayed if the assertion fails.

        Raises:
            AssertResult: If an assertion fails.
    """
    if expected not in collection:
        if message == "":
            message = "{0} not in {1}".format(expected, collection)
        raise AssertResult(assertIn.__name__, message)


def assertNotIn(expected, collection, message=""):
    """Checks whether expected is not in collection.

        Args:
            expected (object): The expected object.
            collection (object): The collection to check in.
            message (Optional[str]): An optional error message,
                that is displayed if the assertion fails.

        Raises:
            AssertResult: If an assertion fails.
    """
    if expected in collection:
        if message == "":
            message = "{0} in {1}".format(expected, collection)
        raise AssertResult(assertNotIn.__name__, message)


def assertRaises(exception, func, *args, message=""):
    """Checks whether func raises an exception of type 'exception'.

        Args:
            exception (Exception): The exception to check for.
            func (Function): The function to execute.
            message (Optional[str]): An optional error message,
                that is displayed if the assertion fails.
            *args (args): The arguments of the function.
    """
    try:
        func(*args)
        if message == "":
            message = "{0} did not raise {1}".format(func.__name__,
                                                     exception.__name__)
        raise AssertResult(assertRaises.__name__, message)
    except exception as e:
        pass


class AssertResult(Exception):
    """The result of an assertion.

        Attributes:
            assertion (str): The name of the assertion that delivered this result.
            message (str): A message that came with the result.
    """

    def __init__(self, assertion, message):
        self.assertion = assertion
        self.message = message
