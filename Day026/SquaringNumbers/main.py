"""
List Comprehension 1
Instructions
You are going to write a List Comprehension to create a new list called squared_numbers. This new list should contain every number in the list numbers but each number should be squared.

e.g. `4 * 4 = 16`
4 squared equals 16.
DO NOT modify the List numbers directly. Try to use List Comprehension instead of a Loop.

Example Output
[1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025]
Hint
Use the keyword method for starting the List comprehension and fill in the relevant parts.

Make sure the squared_numbers is printed into the console for the code checking to work.
"""
#
# Imports
#
import os
from turtle import Turtle, Screen
import pandas as pd


#
# Classes
#

#
# Global variables
#

#
# Private functions
#

# clear_console
def clear_console():
    """
    Clears console.
    """
    command = "clear"
    if os.name in ("nt", "dos"):  # If Machine is running on Windows, use cls
        command = "cls"
    os.system(command)


#
def SquareNumbers(numbers):
    """
    Take a list of numbers, square them and return a list of the squared numbers.-
    """
    return [n ** 2 for n in numbers]


#
# main
#
if __name__ == "__main__":
    # Clear console
    clear_console()


# Import
import unittest

# Create tests
class MyTest(unittest.TestCase):
    # test_1
    def test_1(self):
        squared_numbers = SquareNumbers([0, 1, 2, 3])
        self.assertEqual([0, 1, 4, 9], squared_numbers)


# Run tests
print("\n")
print("Running some tests on the code:")
print(".\n.\n.\n.")
unittest.main(verbosity=1, exit=False)