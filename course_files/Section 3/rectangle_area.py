import argparse

parser = argparse.ArgumentParser(
                    prog = 'Script to calculate the area of a rectangle',
                    description = 'Provide the size of two edges and you will get the area',
                    epilog = 'Enjoy')

parser.add_argument('-l', '--lenght', help="Length.",required=True)
parser.add_argument('-w', '--width', help="Width",required=True)


args = parser.parse_args()

try:
    a = float(args.lenght)
    b = float(args.width)
    area = a*b
    print(f"The area of the rectangle is {a*b}")
except ValueError:
    print("Please introduce a valid number!")
