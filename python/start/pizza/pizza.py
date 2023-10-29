from tabulate import tabulate
import csv
import sys

if len(sys.argv)==2:
    if sys.argv[1][-3:]=="csv":
        try:
            with open(sys.argv[1]) as file:
                lines = csv.DictReader(file)
                print(tabulate(lines, headers="keys", tablefmt="grid"))
        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a CSV file")
if len(sys.argv)>2:
    sys.exit("Too many command-line arguments")
if len(sys.argv)<2:
    sys.exit("Too few command-line arguments")
