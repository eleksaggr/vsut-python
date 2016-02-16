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

## Running units
Units can be run with the test runner, as follows:
```
python runner.py [--format=table] module.TestClass module1.TestClass1 ...
```
The `--format` argument is optional and specifies the method of formatting the output. Available methods are `table` and `csv`, with `table` being the default.

NOTE: The separator for the CSV output can not be specified at the moment. It is always ','.
#### Output as Table
Output as a table can look like this for example:
```
[TestCase]
Id  |           Name            | Status |   Time   |     Assert     | Message
0   | testAssertEqual           |   OK   | 0.000003 |                |
1   | testAssertEqualFail       |   OK   | 0.000008 |                |
2   | testAssertEqualFailFail   |  FAIL  | 0.000002 | None           | The method was expected to fail.
3   | testAssertFalse           |   OK   | 0.000001 |                |
4   | testAssertIn              |   OK   | 0.000002 |                |
5   | testAssertIs              |   OK   | 0.000001 |                |
6   | testAssertIsNone          |   OK   | 0.000002 |                |
7   | testAssertIsNot           |   OK   | 0.000001 |                |
8   | testAssertIsNotNone       |   OK   | 0.000001 |                |
9   | testAssertNotEqual        |   OK   | 0.000001 |                |
10  | testAssertNotIn           |   OK   | 0.000002 |                |
11  | testAssertRaises          |   OK   | 0.000005 |                |
12  | testAssertTrue            |   OK   | 0.000002 |                |
13  | testFailWithCustomMessage |  FAIL  | 0.000003 | assertEqual    | A custom message.
14  | testWillFail              |  FAIL  | 0.000003 | assertEqual    | 1 != 2
15  | testWillFailToo           |  FAIL  | 0.000003 | assertNotEqual | 1 == 1
```

#### Output as CSV
Output as CSV can look like this for example:
```
TestCase
0,testAssertEqual,OK,0.000004
1,testAssertEqualFail,OK,0.000011
2,testAssertEqualFailFail,FAIL,0.000004,None,The method was expected to fail.
3,testAssertFalse,OK,0.000002
4,testAssertIn,OK,0.000004
5,testAssertIs,OK,0.000004
6,testAssertIsNone,OK,0.000002
7,testAssertIsNot,OK,0.000004
8,testAssertIsNotNone,OK,0.000002
9,testAssertNotEqual,OK,0.000003
10,testAssertNotIn,OK,0.000002
11,testAssertRaises,OK,0.000007
12,testAssertTrue,OK,0.000003
13,testFailWithCustomMessage,FAIL,0.000006,assertEqual,A custom message.
14,testWillFail,FAIL,0.000007,assertEqual,1 != 2
15,testWillFailToo,FAIL,0.000006,assertNotEqual,1 == 1
```
