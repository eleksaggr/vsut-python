from vsut.assertion import *
from vsut.unit import Unit


class AssertTest(Unit):

    def setup(self):
        pass

    def teardown(self):
        pass

    def testAssertEqual(self):
        assertEqual(1, 1)
        assertEqual(True, True)
        assertEqual("abc", "abc")

    @Unit.expectFailure
    def testAssertEqualFail(self):
        assertEqual(False, True)

    def testAssertNotEqual(self):
        assertNotEqual(1, 2)
        assertNotEqual(True, False)
        assertNotEqual("abc", "cba")

    @Unit.expectFailure
    def testAssertNotEqualFail(self):
        assertNotEqual(1, 1)

    def testAssertTrue(self):
        assertTrue(True)
        assertTrue(1 == 1)
        assertTrue("abc" == "abc")

    @Unit.expectFailure
    def testAssertTrueFail(self):
        assertTrue(False)

    def testAssertFalse(self):
        assertFalse(False)
        assertFalse(1 != 1)
        assertFalse("abc" != "abc")

    @Unit.expectFailure
    def testAssertFalse(self):
        assertFalse(True)

    def testAssertIs(self):
        a = b = 1
        assertIs(None, None)
        assertIs(1, 1)
        assertIs(a, b)

    @Unit.expectFailure
    def testAssertIsFail(self):
        assertIs(1, None)

    def testAssertIsNot(self):
        assertIsNot(1, 2)
        assertIsNot(1, None)

    @Unit.expectFailure
    def testAssertIsNotFail(self):
        assertIsNot(None, None)

    def testAssertIsNone(self):
        assertIsNone(None)

    @Unit.expectFailure
    def testAssertIsNoneFail(self):
        assertIsNone(1)

    def testAssertIsNotNone(self):
        assertIsNotNone(1)
        assertIsNotNone(True)
        assertIsNotNone("abc")

    @Unit.expectFailure
    def testAssertIsNotNoneFail(self):
        assertIsNotNone(None)

    def testAssertIn(self):
        assertIn(1, [1, 2, 3])
        assertIn("abc", {1: "abc", 2: "bcd"})

    @Unit.expectFailure
    def testAssertIn(self):
        assertIn(2, [1, 3, 4])

    def testAssertNotIn(self):
        assertNotIn(1, [2, 3, 4])
        assertNotIn("abc", {1: "bcd"})

    @Unit.expectFailure
    def testAssertNotInFail(self):
        assertNotIn(1, [1, 2, 3])

    def testAssertRaises(self):
        div = lambda a, b: a / b
        assertRaises(ZeroDivisionError, div, 2, 0)

    @Unit.expectFailure
    def testAssertRaisesFail(self):
        div = lambda a, b: a / b
        assertRaises(ZeroDivisionError, div, 2, 1)
