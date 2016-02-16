from vsut.unit import Unit
from vsut.assertion import assertEqual, assertNotEqual, assertFalse, assertTrue, assertIn, assertNotIn, assertIs, assertIsNot, assertIsNone, assertIsNotNone, assertRaises


class TestCase(Unit):

    # def setup(self):
    #     self.x = 1
    #
    # def teardown(self):
    #     self.x = 0
    #

    def testAssertEqual(self):
        assertEqual(1, 1)

    @Unit.expectFailure
    def testAssertEqualFail(self):
        assertEqual(1, 2)

    @Unit.expectFailure
    def testAssertEqualFailFail(self):
        assertEqual(1, 1)

    def testAssertNotEqual(self):
        assertNotEqual(1, 2)

    def testAssertTrue(self):
        assertTrue(True)

    def testAssertFalse(self):
        assertFalse(False)

    def testAssertIs(self):
        assertIs("a", "a")

    def testAssertIsNot(self):
        assertIsNot("a", "b")

    def testAssertIsNone(self):
        assertIsNone(None)

    def testAssertIsNotNone(self):
        assertIsNotNone(1)

    def testAssertIn(self):
        assertIn(1, [1, 2, 3])

    def testAssertNotIn(self):
        assertNotIn(4, [1, 2, 3])

    def testAssertRaises(self):
        assertRaises(ZeroDivisionError, func, 1, 0)

    def testWillFail(self):
        assertEqual(1,2)

    def testWillFailToo(self):
        assertNotEqual(1,1)

    def testFailWithCustomMessage(self):
        assertEqual(1,2,message="A custom message.")

def func(a, b):
    return a / b
