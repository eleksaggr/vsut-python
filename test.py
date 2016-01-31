from vsut.unit import Case, Suite, test


class TestCase(Case):

    def run(self):
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
        self.failUnless(1, 1)
        self.failUnless(1, 0)

    @test
    def testTestolino(self):
        print("Test called.")
        self.assertEqual(1, 1)


class SecondCase(Case):

    def run(self):
        self.assertEqual("abc", "abc")


def func(a, b):
    return a / b

if __name__ == "__main__":
    s = Suite("TestCase Suite")
    c = TestCase("TestCase")
    c1 = SecondCase("SecondCase")

    c.testTestolino()

    s.add(c)
    s.add(c1)
    s.run(verbose=True)
