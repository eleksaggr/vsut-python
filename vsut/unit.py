from collections import namedtuple
from enum import Enum
from math import floor, log10
from sys import stdout
from time import clock
from vsut.assertion import AssertResult


class Unit():
    """A unit is a group of tests, that are run at once.

    Every method of this class, that starts with 'test' will be run automatically,
    when the run()-method is called.
    Before and after every test the setup and teardown methods will be called respectively.
    For every test it's execution time, status, and if necessary an error message are recorded.

        Attributes:
            tests ({int: str}): A map that maps function names to an unique id.
            times ({int: str}): A map that maps a functions execution time as a string to its id.
            results ({int: AssertResult}): A map that maps a tests result to its id. If a test is successful its entry is None.
    """

    def __init__(self):
        self.tests = {
            id: funcName
            for id, funcName in enumerate([method for method in dir(self)
                                           if callable(getattr(self, method))
                                           and method.startswith("test")])
        }
        self.times = {}
        self.results = {}
        self.failed = False
        self.ignoreUnit = False

    def run(self):
        """Runs all tests in this unit.

            Times the execution of all tests and records them.
        """
        for id, name in self.tests.items():
            # Start timing the tests.
            start = clock()
            try:
                # Get the method that needs to be executed.
                func = getattr(self, name, None)

                # Run the setup method.
                self.setup()
                # Run the test method.
                func()
                # Run the teardown method.
                self.teardown()
            except AssertResult as e:
                result = e
                self.failed = True
            else:
                result = None
            self.results[id] = result

            # Add the execution time of the test to the times map.
            elapsed = clock() - start
            self.times[id] = "{0:.6f}".format(elapsed)

    def setup(self):
        """Setup is executed before every test.
        """
        pass

    def teardown(self):
        """Teardown is executed after every test.
        """
        pass
