import sys
import csv
from tabulate import tabulate

def main():

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too mant command-line arguments")
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")


    try:
        with open (sys.argv[1]) as file:
            table=csv.reader(file)
            print(tabulate(table, headers="firstrow", tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__=="__main__":
    main()