from collections import namedtuple
from enum import Enum
from sys import stdout

Result = namedtuple('Result', 'id status message')
Status = Enum('Status', 'Ok, Fail, Error')


class Suite:

    def __init__(self, name):
        self.name = name
        self.cases = []

    def add(self, case):
        if case is not None and isinstance(case, Case):
            self.cases.append(case)

    def run(self, out=stdout):
        results = []
        id = 0
        for case in self.cases:
            result = None
            try:
                case.run()
                result = Result(id, Status('Ok'), "\t\t")
            except AssertionError as e:
                result = Result(id, Status('Fail'), e)
            except FailError as e:
                # Should we run into a fail condition exit the loop.
                result = Result(id, Status('Error'), e)
                results.append(result)
                break

            results.append(result)
            id = id + 1

        print("Suite: {0}".format(self.name), file=out)
        for result in results:
            print("{0}: {1} ({2})".format(
                result.id, result.message, result.status), file=out)


class Case:

    def run(self):
        pass

    def assertEqual(value, expected):
        if value != expected:
            raise AssertionError("{0} is not {1}".format(value, expected))

    def failUnless(value, expected):
        if value != expected:
            raise FailError("{0} is not {1}".format(value, expected))

class FailError(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
