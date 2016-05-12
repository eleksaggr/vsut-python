from vsut.unit import Unit


class Formatter():
    """A Formatter formats the results of a unit for viewing.
    """

    def format(self, unit):
        """Formats the result of a unit.
        """
        pass


class TableFormatter(Formatter):
    """A TableFormatter formats the results of a unit as a table.

    The table looks as follows:
    Id | Name | Status | Time | Assert | Message

    NOTE: The TableFormatter currently only supports up to 999 test ids, as its id column width is fixed to 3.
            Please refrain from ever running more than 999 tests. That's crazy.
    """

    def format(self, unit):

        # Get the maximum length of the name attribute.
        nameLength = max([len(name) for name in unit.tests.values()])
        # Get the maximum length of the assertion attribute.
        if len([result for result in unit.results.values() if result is
                not None]) != 0:
            assertLength = max([len(result.assertion)
                                for result in unit.results.values()
                                if result is not None])
        else:
            assertLength = 6

        # Add the name of the unit.
        ret = "[{0}]\n".format(type(unit).__name__)
        # Add the table header.
        ret += "{0:^3} | {1:^{nameLength}} | {2:^6} | {3:^8} | {4:^{assertLength}} | {5}\n".format(
            "Id",
            "Name",
            "Status",
            "Time",
            "Assert",
            "Message",
            nameLength=nameLength,
            assertLength=assertLength)

        for id, name in unit.tests.items():
            result = unit.results[id]
            if result == None:
                ret += "{0:<3} | {1:<{nameLength}} | {2:^6} | {3:<8} | {4:<{assertLength}} |\n".format(
                    id,
                    name,
                    "OK",
                    unit.times[id],
                    "",
                    nameLength=nameLength,
                    assertLength=assertLength)
            else:
                ret += "{0:<3} | {1:<{nameLength}} | {2:^6} | {3:<8} | {4:<{assertLength}} | {5}\n".format(
                    id,
                    name,
                    "FAIL",
                    unit.times[id],
                    result.assertion,
                    result.message,
                    nameLength=nameLength,
                    assertLength=assertLength)
        return ret


class CSVFormatter(Formatter):
    """A CSVFormatter formats the result of a unit as a comma-separated-values list.

        Its separator can be specified when formatting, the default value is ','.
    """

    def __init__(self, separator=";"):
        self.separator = separator

    def format(self, unit):
        """Formats the results of a unit.
        """
        ret = "{0}\n".format(type(unit).__name__)

        for id, name in unit.tests.items():
            result = unit.results[id]
            if result is None:
                ret += "{1}{0}{2}{0}OK{0}{3}\n".format(self.separator, id, name,
                                                       unit.times[id])
            else:
                ret += "{1}{0}{2}{0}FAIL{0}{3}{0}{4}{0}{5}\n".format(
                    self.separator, id, name, unit.times[id], result.assertion,
                    result.message)
        return ret
