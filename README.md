# **V**ery **S**imple **U**nit **T**est
**VSUT** is a simple unit test framework for Python.

## Usage
A unit can be described as a test-case, like follows:
```python
...
class UnitTest(vsut.unit.Case):

    def testComponentOne(self):
        ...
    def testComponentTwo(self):
        ...
```
Any methods that start with 'test' will be executed automatically, once the case is run.

## Asserts & Fail Conditions
The following methods can be used in a test-case to check for success or failure:
* ```assertEqual(value, expected)``` - Checks for equality of the two arguments.
* ```assertNotEqual(value, expected)``` - Checks for inequality of the two arguments.
* ```assertTrue(value)``` - Checks whether the argument is the boolean value True.
* ```assertFalse(value)``` - Checks whether the argument is the boolean value False.
* ```assertIn(value, collection)``` - Checks whether the argument is in the collection.
* ```assertNotIn(value, collection)``` - Checks whether the argument is not in the collection.
* ```assertIs(value, expected)``` - Checks whether the value is the expected.
* ```assertIsNot(value, expected)``` - Checks whether the value is not the expected.
* ```assertIsNone(value)``` - Checks whether the argument is None.
* ```assertIsNotNone(value)``` - Checks whether the argument is not None.
* ```assertRaises(exception, func, *args, **kwargs)``` - Checks whether the function 'func' raises an exception of the type 'exception'.

## Full Example
```python
from vsut.unit import Case

class TestCase(Case):

    def testExample(self):
        a = True
        b = True
        c = False
        self.assertEqual(a, b)
        self.assertEqual(b, c)

if __name__ == "__main__":
    case = TestCase("Case 1")
    case.run()
```

## Output
```
Case: Case 1
-------------------------------------------------------------------------
[0] testExample: Status.Ok   |[assertEqual]
[0] testExample: Status.Fail |[assertEqual] -> True is not equal to False
-------------------------------------------------------------------------
```
