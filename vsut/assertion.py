def assertEqual(expected, actual, message=""):
    """Checks whether expected is equal to actual.

        Args:
            expected (object): The expected object.
            actual (object): The actual object.
            message (Optional[str]): An optional error message,
                that is displayed if the assertion fails.

        Raises:
            AssertException: If an assertion fails.
    """
    if expected != actual:
        if message == "":
            message = "{0} != {1}".format(expected, actual)
        raise AssertException(assertEqual, message)


def assertNotEqual(expected, actual, message=""):
    """Checks whether expected is not equal to actual.

        Args:
            expected (object): The expected object.
            actual (object): The actual object.
            message (Optional[str]): An optional error message,
                that is displayed if the assertion fails.

        Raises:
            AssertException: If an assertion fails.
    """
    if expected == actual:
        if message == "":
            message = "{0} == {1}".format(expected, actual)
        raise AssertException(assertNotEqual, message)


def assertTrue(expected, message=""):
    """Checks whether expected is equal to True.

        Args:
            expected (object): The expected object.
            message (Optional[str]): An optional error message,
                that is displayed if the assertion fails.

            Raises:
                AssertException: If an assertion fails.
    """
    if expected != True:
        if message == "":
            message = "{0} != True".format(expected)
        raise AssertException(assertTrue, message)


def assertFalse(expected, message=""):
    """Checks whether expected is equal to False.

        Args:
            expected (object): The expected object.
            message (Optional[str]): An optional error message,
                that is displayed if the assertion fails.

        Raises:
            AssertException: If an assertion fails.
    """
    if expected != False:
        if message == "":
            message = "{0} != False".format(expected)
        raise AssertException(assertFalse, message)


def assertIs(expected, actual, message=""):
    """Checks whether expected is actual.

        Args:
            expected (object): The expected object.
            actual (object): The actual object.
            message (Optional[str]): An optional error message,
                that is displayed if the assertion fails.

        Raises:
            AssertException: If an assertion fails.
    """
    if expected is not actual:
        if message == "":
            message = "{0} is not {1}".format(expected, actual)
        raise AssertException(assertIs, message)


def assertIsNot(expected, actual, message=""):
    """Checks whether expected is not actual.

        Args:
            expected (object): The expected object.
            actual (object): The actual object.
            message (Optional[str]): An optional error message,
                that is displayed if the assertion fails.

        Raises:
            AssertException: If an assertion fails.
    """
    if expected is actual:
        if message == "":
            message = "{0} is {1}".format(expected, actual)
        raise AssertException(assertIsNot, message)


def assertIsNone(expected, message=""):
    """Checks whether expected is None.

        Args:
            expected (object): The expected object.
            message (Optional[str]): An optional error message,
                that is displayed if the assertion fails.

        Raises:
            AssertException: If an assertion fails.
    """
    if expected != None:
        if message == "":
            message = "{0} is not None".format(expected)
        raise AssertException(assertIsNone, message)


def assertIsNotNone(expected, message=""):
    """Checks whether expected is not None.

        Args:
            expected (object): The expected object.
            message (Optional[str]): An optional error message,
                that is displayed if the assertion fails.

        Raises:
            AssertException: If an assertion fails.
    """
    if expected == None:
        if message == "":
            message = "{0} is None".format(expected)
        raise AssertException(assertIsNotNone, message)


def assertIn(expected, collection, message=""):
    """Checks whether expected is in collection.

        Args:
            expected (object): The expected object.
            collection (object): The collection to check in.
            message (Optional[str]): An optional error message,
                that is displayed if the assertion fails.

        Raises:
            AssertException: If an assertion fails.
    """
    if expected not in collection:
        if message == "":
            message = "{0} not in {1}".format(expected, collection)
        raise AssertException(assertIn, message)


def assertNotIn(expected, collection, message=""):
    """Checks whether expected is not in collection.

        Args:
            expected (object): The expected object.
            collection (object): The collection to check in.
            message (Optional[str]): An optional error message,
                that is displayed if the assertion fails.

        Raises:
            AssertException: If an assertion fails.
    """
    if expected in collection:
        if message == "":
            message = "{0} in {1}".format(expected, collection)
        raise AssertException(assertNotIn, message)


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
            message = "{0} did not raise {1}".format(
                func.__name__, exception.__name__)
        raise AssertException(assertRaises, message)
    except exception as e:
        pass


class AssertException(Exception):

    def __init__(self, assertion, message):
        self.assertion = assertion
        self.message = message
