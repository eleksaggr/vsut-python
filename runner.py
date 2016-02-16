import argparse
import sys
from vsut.unit import CSVFormatter, TableFormatter, Unit

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Runs unit tests.")
    parser.add_argument('units', metavar='Unit', type=str, nargs='+')
    parser.add_argument(
        '--format', help="Default: table; Decides whether to use table or csv for output.", required=False)
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
                formatter = CSVFormatter(unit)
            else:
                formatter = TableFormatter(unit)
            print(formatter)
        except (ImportError, AttributeError) as e:
            print("[Error] Could not import unit: {0}".format(unit))
