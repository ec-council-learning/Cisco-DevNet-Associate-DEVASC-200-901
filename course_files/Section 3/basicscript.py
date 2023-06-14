
try:
    x = input("Please provide a number to divide 4 with")
    x = int(x)
    print(4/x)
except ValueError:
    print("Please introduce a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")