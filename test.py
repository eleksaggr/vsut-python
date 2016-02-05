from vsut.unit import Case


class TestCase(Case):

    def setup(self):
        self.x = 1

    def teardown(self):
        self.x = 0

    def testAll(self):
        self.assertEqual(1, 1)
        self.assertEqual(1, 2)
        self.assertNotEqual(1, 2)
        self.assertNotEqual(1, 1)
        self.assertTrue(True)
        self.assertTrue(False)
        self.assertFalse(False)
        self.assertFalse(True)
        self.assertIs("abc", "abc")
        self.assertIs("abc", "cba")
        self.assertIsNot("abc", "cba")
        self.assertIsNot("abc", "abc")
        self.assertIsNone(None)
        self.assertIsNone(1)
        self.assertIsNotNone(1)
        self.assertIsNotNone(None)
        self.assertIn(1, [1, 2, 3])
        self.assertIn(4, [1, 2, 3])
        self.assertNotIn(4, [1, 2, 3])
        self.assertNotIn(1, [1, 2, 3])
        self.assertRaises(ZeroDivisionError, func, 1, 0)
        self.assertRaises(ZeroDivisionError, func, 1, 1)

    def testNumberTwo(self):
        self.assertEqual(1, 1)

    def testSetupAndTeardown(self):
        self.assertEqual(self.x, 1)
        self.x = 2
        self.y = 3

    def testSetupAndTeardownTwo(self):
        self.assertNotEqual(self.x, 2)
        self.assertEqual(self.y, 3)

    # def testAlignmentOnOutputThisMustBeLong(self):
    #     self.assertEqual(1, 1)


def func(a, b):
    return a / b

if __name__ == "__main__":
    c = TestCase("TestCase")
    c.run()
