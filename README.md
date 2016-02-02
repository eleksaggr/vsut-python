# vsut-python

## Usage

#### Example Testcase
Defining a testcase:
```python
from vsut.unit import Case

class TestCase(Case):

    def testExample():
        assert(a, b)
        ...
```
All methods that start with 'test' will automatically be executed, when the Suite is run.
#### Full example
```python
from vsut.unit import Case, Suite

class TestCase(Case):

    def testExample():
        assert(a, b)

if __name__ == "__main__":
    suite = Suite()
    case = TestCase()

    suite.add(case)

    suite.run()
```

When calling run() on the Suite one can specifiy a preferred output stream and whether the ouput should be verbose.

```python
def run(self, out=stdout, verbose=True):
    ...
```
