import argparse
import sys
from vsut.unit import CSVFormatter, TableFormatter, Unit

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Runs unit tests and outputs them to the terminal.")
    parser.add_argument('units', metavar='Unit', type=str, nargs='+')
    parser.add_argument(
        '--format', help="Whether the output shall be formatted as a table or as csv-data. (Default: table)", required=False)
    parser.add_argument('--separator', help="If the output format is csv, the separator character can be specified by this."
        " (NOTE: Certain characters are special characters in UNIX terminals and must be prefaced by \)", required=False)
    args = vars(parser.parse_args())

    for unit in args["units"]:
        try:
            # Get the name of the module.
            modName = unit.split(".")[0:-1]
            modName = ".".join(modName)

            # Get the name of the class.
            className = unit.split(".")[-1]

            # Import the module.
            module = __import__(modName, fromlist=[className])

            # Create unit and run it.
            unit = getattr(module, className)()
            unit.run()

            # Format the results and output them.
            if args["format"] == "csv":
                if args["separator"] is not None and args["separator"] != "":
                    formatter = CSVFormatter(unit, args["separator"])
                else:
                    formatter = CSVFormatter(unit)
            else:
                formatter = TableFormatter(unit)
            print(formatter)
        except (ImportError, AttributeError) as e:
            print("[Error] Could not import unit: {0}".format(unit))
            print(e)
