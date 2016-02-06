import sys
from vsut.unit import TableFormatter

if __name__ == "__main__":
    for i in range(1, len(sys.argv)):
        try:
            modName = sys.argv[i].split(".")[0:-1]
            modName = ".".join(modName)

            className = sys.argv[i].split(".")[-1]
            module = __import__(modName, fromlist=[className])

            className = getattr(module, className)

            unit = className()
            unit.run()

            formatter = TableFormatter(unit)
            formatter.print()
        except ImportError as e:
            #TODO: Handle this import error.
            print(e)
