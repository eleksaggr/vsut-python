import argparse
import os, os.path
import sys
from vsut.unit import CSVFormatter, TableFormatter, Unit


def main():
    sys.path.append(os.getcwd())

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
        if path.endswith("/"):
            # Path is a directory.
            files = [f[0:-3]
                     for f in os.listdir(path)
                     if os.path.isfile(os.path.join(path, f))]
        else:
            # Path is a file.
            files = [path[0:-3]]

        modules = []
        for file in files:
            # Transform path to module name.
            modules.append(path[0:-1] + "." + file.replace("/", "."))

        classes = loadClasses(modules)

        # Find out which formatter to use.
        if args["format"] == "csv":
            formatter = CSVFormatter
        else:
            formatter = TableFormatter

        # Find out which separator to use for CSV.
        if args["separator"] is not None and args["separator"] != "":
            separator = args["separator"]
        else:
            separator = ";"

        ret = runTests(classes, formatter, separator)
        if ret:
            returnValue = True

    if returnValue:
        sys.exit(1)


def loadClasses(modules):
    try:
        for module in modules:
            __import__(module)

        return Unit.__subclasses__()
    except (ImportError, AttributeError) as e:
        print("[Error] Could not import module: {0}".format(module))
        print(e)


def runTests(classes, formatterCls, separator):
    failure = False
    for cls in classes:
        unit = cls()
        unit.run()

        if unit.failed:
            failure = True

        #NOTE: This looks weird. There should be a way to get the class as
        # argument and instanciate it.
        if formatterCls == CSVFormatter:
            formatter = CSVFormatter(unit, separator)
        else:
            formatter = TableFormatter(unit)

        formatter.format()
        print(formatter)

    return failure


if __name__ == "__main__":
    main()
