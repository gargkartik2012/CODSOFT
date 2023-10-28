# A simple calculator with basic arithmetic operations in python

# A function to perform addition
def add(x, y):
    return x + y

# A function to perform subtraction
def subtract(x, y):
    return x - y

# A function to perform multiplication
def multiply(x, y):
    return x * y

# A function to perform division
def divide(x, y):
    return x / y

# A dictionary to store the operation symbols and functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# A loop to prompt the user to input two numbers and an operation choice
while True:
    # Display the available operations
    print("Available operations:")
    for symbol in operations:
        print(symbol)

    # Ask the user to choose an operation
    choice = input("Enter your choice of operation (or q to quit): ")

    # Check if the user wants to quit
    if choice == "q":
        print("Thank you for using the calculator.")
        break

    # Check if the user entered a valid operation symbol
    if choice not in operations:
        print("Invalid operation. Please try again.")
        continue

    # Ask the user to enter two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform the calculation and display the result
    result = operationschoice
    print(f"The result of {num1} {choice} {num2} is {result}.")
