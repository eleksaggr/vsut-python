import argparse
import os, os.path
import sys

from vsut.format import CSVFormatter, TableFormatter
from vsut.unit import Unit


def main():
    sys.path.insert(0, os.getcwd())

    parser = argparse.ArgumentParser(
        description="Runs unit tests and outputs them to the terminal.")
    parser.add_argument('files', metavar='Files', type=str, nargs='+')
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

    returnValue = False

    for path in args["files"]:
        files = findFiles(path)

        modules = []
        for file in files:
            # Transform path to module name.
            modules.append(file.replace("/", ".")[0:-3])

        classes = loadClasses(modules)

        # Find out which formatter to use.
        if args["format"] == "csv":
            separator = ";"
            if args["separator"] is not None and args["separator"] != "":
                separator = args["separator"]
            formatter = CSVFormatter(separator)
        else:
            formatter = TableFormatter()

        ret = runTests(classes, formatter)
        if ret:
            returnValue = True

    if returnValue:
        sys.exit(1)

def findFiles(path):
    files = []
    if os.path.isdir(path):
        for file in os.listdir(path):
            if not path.endswith("/"):
                path = path + "/"
            files.extend(findFiles(path + file))
    else:
        if path.endswith(".py"):
            files.append(path) # Return file name
    return files

def loadClasses(modules):
    try:
        for module in modules:
            __import__(module)

        return Unit.__subclasses__()
    except (ImportError, AttributeError) as e:
        print("[Error] Could not import module: {0}".format(module))
        print(e)


def runTests(classes, formatter=None, strict=False):
    failure = False
    for cls in classes:
        unit = cls()
        if not unit.ignoreUnit or strict:
            unit.run()

            if unit.failed:
                failure = True

            if formatter is not None:
                print(formatter.format(unit))

    return failure


if __name__ == "__main__":
    main()
