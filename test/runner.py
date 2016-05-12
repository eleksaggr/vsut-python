from runner import loadClasses, runTests

from vsut.assertion import assertEqual, assertTrue, assertFalse, assertIn
from vsut.unit import Unit

class RunnerTest(Unit):

    def testLoadClasses(self):
        modules = ["test.runner"]
        classes = loadClasses(modules)

        assertIn(type(self), classes)

    def testRunTests(self):
        success = [RunnerTest.MockUnitSuccess]
        fail = [RunnerTest.MockUnitFail]
        assertFalse(runTests(success, strict=True))
        assertTrue(runTests(fail, strict=True))

    class MockUnitSuccess(Unit):

        def __init__(self):
            super().__init__()
            self.ignoreUnit = True

        def testSuccess(self):
            assertEqual(1, 1)

    class MockUnitFail(Unit):

        def __init__(self):
            super().__init__()
            self.ignoreUnit = True

        def testFailure(self):
            assertEqual(1, 2)
