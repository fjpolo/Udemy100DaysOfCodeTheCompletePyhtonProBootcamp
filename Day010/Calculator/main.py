"""


"""
#
# Imports
#
import random
from art import logo
import os

#
# Private functions
#

# clearConsole
def clearConsole():
    """
    Clears console.
    """
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

# Add
def Add(n1, n2):
    """
    Takes two numbers and returns its addition.-
    """
    return (n1+n2)

# Substract
def Substract(n1, n2):
    """
    Takes two numbers and returns its substraction.-
    """
    return (n1-n2)

# Multiply
def Multiply(n1, n2):
    """
    Takes two numbers and returns its product.-
    """
    return (n1*n2)

# Divide
def Divide(n1, n2):
    """
    Takes two numbers and returns its division.-
    """
    if n2 == 0:
        return "Error!Cannot divide by Zero!"
    return (n1/n2)

# calculator
def calculator():
    """
    Calculator funciton.
    """
    print(logo)
    num1 = float(input("What's the first number?: "))
    for operator in operations:
      print(operator)
    shouldContinue = True


    while shouldContinue:
        operationSymbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        function = operations[operationSymbol]
        answer = function(num1, num2)
        print(f"{num1} {operationSymbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            shouldContinue = False
            clearConsole()
      

#
# Global variables
#

#
operations = {
                "+": Add,
                "-": Substract,
                "*": Multiply,
                "/": Divide
             }

#
# main
#
if __name__ == "__main__":
    # Call function
    calculator()


