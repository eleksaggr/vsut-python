# **V**ery **S**imple **U**nit **T**est
**VSUT** is a simple unit test framework for Python.

## Usage
A unit can be described , like follows:
```python
...
class UnitTest(vsut.unit.Unit):

    def testComponentOne(self):
        ...
    def testComponentTwo(self):
        ...
```
Any methods that start with 'test' will be executed automatically, once the case is run.

## Asserts & Fail Conditions
The following methods can be used in a test-case to check for success or failure:
* ```assertEqual(expected, actual)``` - Checks for equality of the two arguments.
* ```assertNotEqual(expected, actual)``` - Checks for inequality of the two arguments.
* ```assertTrue(expected)``` - Checks whether the argument is the boolean value True.
* ```assertFalse(expected)``` - Checks whether the argument is the boolean value False.
* ```assertIn(expected, collection)``` - Checks whether the argument is in the collection.
* ```assertNotIn(expected, collection)``` - Checks whether the argument is not in the collection.
* ```assertIs(expected, actual)``` - Checks whether the value is the expected.
* ```assertIsNot(expected, actual)``` - Checks whether the value is not the expected.
* ```assertIsNone(expected)``` - Checks whether the argument is None.
* ```assertIsNotNone(expected)``` - Checks whether the argument is not None.
* ```assertRaises(exception, func, *args)``` - Checks whether the function 'func' raises an exception of the type 'exception'.

For any of these methods a **message** parameter can be specified, that will be printed instead of the default message.
#### Example
```python
...
assertEqual(True, False, message="True is not False")
...
```

## Expected Failures
A test can be annotated with the `expectedFailure` decorator, as follows:
```python
...
    @Unit.expectedFailure
    def testThatWillFail(self):
        ...
...
```
Upon execution the unit will check, if the test really failed.
Should this not be the case the test will be listed as a failure.

## Full Example
```python
from vsut.unit import Unit
from vsut.assertion import assertEqual

class TestCase(Unit):

    def testExample(self):
        a = True
        b = True
        c = False
        assertEqual(a, b)
        assertEqual(b, c)
```
Run it with the test runner:
```
python runner.py module.TestClass module1.TestClass1 ...
```

#### Output
```
[TestCase]
Id  |    Name     | Status |   Time   |   Assert    | Message
0   | testExample |  FAIL  | 0.000027 | assertEqual | True != False
```
