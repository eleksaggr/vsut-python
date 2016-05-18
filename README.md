# Very Simple Unit Testing [![Build Status](https://travis-ci.org/zillolo/vsut-python.svg?branch=master)](https://travis-ci.org/zillolo/vsut-python)

## Introduction
**VSUT** is a simple unit-testing framework for Python 3.4.

## Installation
To install **VSUT** use the following command:
```
pip install vsut
```

## Usage
A unit is represented as a subclass of the `Unit` class. Any methods defined in the unit, whose names start with `test` (case-sensitive) will be executed, when the unit is run.

An example of this could look as follows:
```python
class UnitTest(vsut.unit.Unit):

    def testOne(self):
        pass

    def testTwo(self):
        pass
```
Additionally `Unit` provides two special methods `setup` and `teardown`. Both can be overridden by implementing them in the unit subclass.
Their effects are:
* `setup` - Runs before *every* test in the unit.
* `teardown` - Runs after *every* test in the unit.

## API
The following functions are available in `vsut.assertion`:

#### assertEqual
Checks for equality of `expected` and `actual`.
* `expected` - The expected value to check against.
* `actual` - The actual value to be checked.
* `message` - A message to be printed in case the check fails.
```python
assertEqual(expected, actual, message="")
```
### assertNotEqual
Checks for inequality of `expected` and `actual`.
* `expected` - The expected value to check against.
* `actual` - The actual value to be checked.
* `message` - A message to be printed in case the check fails.
```python
assertNotEqual(expected, actual, message="")
```
### assertTrue
Checks whether `actual` is `True`.
* `actual` - The actual value to be checked.
* `message` - A message to be printed in case the check fails.
```python
assertTrue(actual, message="")
```
### assertFalse
Checks whether `actual` is `False`.
* `actual` - The actual value to be checked.
* `message` - A message to be printed in case the check fails.
```python
assertFalse(actual, message="")
```
### assertIn
Checks whether `expected` is in the collection `collection`.
* `collection` - The collection to search in.
* `actual` - The value to be searched.
* `message` - A message to be printed in case the check fails.
```python
assertIn(expected, collection, message="")
```
### assertNotIn
Checks whether `expected` is not in the collection `collection`.
* `collection` - The collection to search in.
* `actual` - The value to be searched.
* `message` - A message to be printed in case the check fails.
```python
assertNotIn(expected, collection, message="")
```
#### assertIs
Checks whether `actual` is `expected`.
* `expected` - The expected value to check against.
* `actual` - The actual value to be checked.
* `message` - A message to be printed in case the check fails.
```python
assertIs(expected, actual, message="")
```
#### assertIsNot
Checks whether `actual` is not `expected`.
* `expected` - The expected value to check against.
* `actual` - The actual value to be checked.
* `message` - A message to be printed in case the check fails.
```python
assertIsNot(expected, actual, message="")
```
### assertIsNone
Checks whether `actual` is `None`.
* `actual` - The actual value to be checked.
* `message` - A message to be printed in case the check fails.
```python
assertIsNone(actual, message="")
```
### assertIsNotNone
Checks whether `actual` is not `None`.
* `actual` - The actual value to be checked.
* `message` - A message to be printed in case the check fails.
```python
assertIsNotNone(actual, message="")
```
### assertRaises
Checks whether `func` raises an object of class `expection`, when called with the parameters specified in `args`.
* `expection` - A class of an exception, that should be raised.
* `func` - The function to be called.
* `args` - The arguments to call `func` with.
```python
assertIsNone(exception, func, *args)
```

## Example
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

## Run tests
Units can be run with the delivered script `vrun`.

#### Usage
`vrun` follows the following signature:
```
vrun [--format=table] test.py tests/test_other.py ...
```
`vrun` takes a list of Python files containing units or a whole directory as parameters. If a directory is specified, all files containing units will be executed (this includes those in sub-directories).

The `--format` argument is optional and specifies the method of formatting the output.
The following are the currently available output methods:
* `table` (default) - Formats the results of the run as a table.
* `csv` - Formats the results of the run as comma-separated values. To specify a separator different from `;`, specify the following argument: `--separator=[your separator]`.

#### Formatting examples
##### Table
```
[TestCase]
Id  |           Name            | Status |   Time   |     Assert     | Message
0   | testAssertEqual           |   OK   | 0.000003 |                |
1   | testAssertEqualFail       |   OK   | 0.000008 |                |
2   | testAssertFalse           |   OK   | 0.000001 |                |
3   | testAssertIn              |   OK   | 0.000002 |                |
4   | testAssertIs              |   OK   | 0.000001 |                |
5   | testAssertIsNone          |   OK   | 0.000002 |                |
6   | testAssertIsNot           |   OK   | 0.000001 |                |
7   | testAssertIsNotNone       |   OK   | 0.000001 |                |
8   | testAssertNotEqual        |   OK   | 0.000001 |                |
9   | testAssertNotIn           |   OK   | 0.000002 |                |
10  | testAssertRaises          |   OK   | 0.000005 |                |
11  | testAssertTrue            |   OK   | 0.000002 |                |
12  | testFailWithCustomMessage |  FAIL  | 0.000003 | assertEqual    | A custom message.
13  | testWillFail              |  FAIL  | 0.000003 | assertEqual    | 1 != 2
14  | testWillFailToo           |  FAIL  | 0.000003 | assertNotEqual | 1 == 1
```

##### CSV
```
TestCase
0,testAssertEqual,OK,0.000004
1,testAssertEqualFail,OK,0.000011
2,testAssertFalse,OK,0.000002
3,testAssertIn,OK,0.000004
4,testAssertIs,OK,0.000004
5,testAssertIsNone,OK,0.000002
6,testAssertIsNot,OK,0.000004
7,testAssertIsNotNone,OK,0.000002
8,testAssertNotEqual,OK,0.000003
9,testAssertNotIn,OK,0.000002
10,testAssertRaises,OK,0.000007
11,testAssertTrue,OK,0.000003
12,testFailWithCustomMessage,FAIL,0.000006,assertEqual,A custom message.
13,testWillFail,FAIL,0.000007,assertEqual,1 != 2
14,testWillFailToo,FAIL,0.000006,assertNotEqual,1 == 1
```

## License
The MIT License (MIT)

Copyright (c) 2016 Alex Egger

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
