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

    def testAssertEqualFail(self):
        assertRaises(AssertResult, assertEqual, False, True)

    def testAssertNotEqual(self):
        assertNotEqual(1, 2)
        assertNotEqual(True, False)
        assertNotEqual("abc", "cba")

    def testAssertNotEqualFail(self):
        assertRaises(AssertResult, assertNotEqual, True, True)

    def testAssertTrue(self):
        assertTrue(True)
        assertTrue(1 == 1)
        assertTrue("abc" == "abc")

    def testAssertTrueFail(self):
        assertRaises(AssertResult, assertTrue, False)

    def testAssertFalse(self):
        assertFalse(False)
        assertFalse(1 != 1)
        assertFalse("abc" != "abc")

    def testAssertFalse(self):
        assertRaises(AssertResult, assertFalse, True)

    def testAssertIs(self):
        a = b = 1
        assertIs(None, None)
        assertIs(1, 1)
        assertIs(a, b)

    def testAssertIsFail(self):
        assertRaises(AssertResult, assertIs, 1, None)

    def testAssertIsNot(self):
        assertIsNot(1, 2)
        assertIsNot(1, None)

    def testAssertIsNotFail(self):
        assertRaises(AssertResult, assertIsNot, True, True)

    def testAssertIsNone(self):
        assertIsNone(None)

    def testAssertIsNoneFail(self):
        assertRaises(AssertResult, assertIsNone, True)

    def testAssertIsNotNone(self):
        assertIsNotNone(1)
        assertIsNotNone(True)
        assertIsNotNone("abc")

    def testAssertIsNotNoneFail(self):
        assertRaises(AssertResult, assertIsNotNone, None)

    def testAssertIn(self):
        assertIn(1, [1, 2, 3])

    def testAssertInFail(self):
        assertRaises(AssertResult, assertIn, 1, [2, 3])

    def testAssertNotIn(self):
        assertNotIn(1, [2, 3, 4])

    def testAssertNotInFail(self):
        assertRaises(AssertResult, assertNotIn, 1, [1, 2])

    def testAssertRaises(self):
        div = lambda a, b: a / b
        assertRaises(ZeroDivisionError, div, 2, 0)

    def testAssertRaisesFail(self):
        div = lambda a, b: a / b
        assertRaises(AssertResult, assertRaises, ZeroDivisionError, div, 2, 1)
