import argparse
import os, os.path
import sys
from vsut.unit import CSVFormatter, TableFormatter, Unit


def main():
    sys.path.append(os.getcwd())

    parser = argparse.ArgumentParser(
        description="Runs unit tests and outputs them to the terminal.")
    parser.add_argument('units', metavar='Unit', type=str, nargs='+')
    parser.add_argument(
        '--format',
        help=
        "Whether the output shall be formatted as a table or as csv-data. (Default: table)",
        required=False)
    parser.add_argument(
        '--separator',
        help=
        "If the output format is csv, the separator character can be specified by this."
        " (NOTE: Certain characters are special characters in UNIX terminals and must be prefaced by \)",
        required=False)
    args = vars(parser.parse_args())

    returnValue = 0
    for unit in args["units"]:
        # Treat units as file names or directory names.
        if unit.endswith("/"):
            # Unit is a directory.
            files = [f[0:-3]
                     for f in os.listdir(unit)
                     if os.path.isfile(os.path.join(unit, f))]

            print(files)
            for file in files:
                module = unit[0:-1] + "." + file.replace("/", ".")
                print(module)
                __import__(module)
            units = Unit.__subclasses__()
            ret = runUnits(units, args)
            if ret != 0:
                returnValue = 1
        else:
            # Unit is a file.
            module = unit.replace("/", ".")[0:-3]
            units = loadUnits(module)
            return runUnits(units, args)

    return returnValue


def loadUnits(module):
    try:
        # Import the module.
        module = __import__(module)

        return Unit.__subclasses__()
    except (ImportError, AttributeError) as e:
        print("[Error] Could not import unit: {0}".format(module))
        print(e)


def runUnits(units, args):
    ret = 0
    for unit in units:
        unit = unit()
        unit.run()

        if unit.failed:
            ret = 1

        # Format the results and output them.
        if args["format"] == "csv":
            if args["separator"] is not None and args["separator"] != "":
                formatter = CSVFormatter(unit, args["separator"])
            else:
                formatter = CSVFormatter(unit)
        else:
            formatter = TableFormatter(unit)
        print(formatter)
    return ret


if __name__ == "__main__":
    main()
