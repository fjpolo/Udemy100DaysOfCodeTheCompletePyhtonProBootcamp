# Instructions
# Read this the code in main.py
# Spot the problems 🐞.
# Modify the code to fix the program.
# Fix the code so that it works and passes the tests when you submit.

# Hint
# Review the previous lesson and go through the 10 steps to tackle these debugging problems.


#
# Imports
#
import os

#
# Global variables
#


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


#
# main
#
if __name__ == "__main__":
    number = int(input("Which number do you want to check?"))
    if number % 2 == 0:
        print("This is an even number.")
    else:
        print("This is an odd number.")