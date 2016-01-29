class TestCase:

    def assertEqual(self, value, expected):
        if value != expected:
            raise CaseFailed("{0} != {1}".format(value, expected))

    def assertTrue(self, value):
        assertEqual(value, True)

    def assertFalse(self, value):
        assertEqual(value, False)

class CaseFailed(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
