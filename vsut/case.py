class TestCase:

    def assertEqual(value, expected):
        if value != expected:
            raise CaseFailed("{0} != {1}")

    def assertTrue(value):
        assertEqual(value, True)

    def assertFalse(value):
        assertEqual(value, False)

class CaseFailed(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return message
