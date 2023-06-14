import argparse

parser = argparse.ArgumentParser(
                    prog = 'My test script with command line parameters',
                    description = 'This is and exercise',
                    epilog = 'Enjoy')

parser.add_argument('-n', '--number', help="Number to divide 4 with.",required=True)      # option that takes a value
parser.add_argument('-v', '--verbose',
                    action='store_true', help="Print details about code execution")  # on/off flag

args = parser.parse_args()

try:
    x = args.number
    x = int(x)
    if args.verbose:
        print(f"Will divide now 4 with {x}")
    print(4/x)
except ValueError:
    print("Please introduce a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")