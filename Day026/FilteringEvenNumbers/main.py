"""
List Comprehension 2
Instructions
You are going to write a List Comprehension to create a new list called result. This new list should only contain the even numbers from the list numbers.

DO NOT modify the List numbers directly. Try to use List Comprehension instead of a Loop.

Example Output
[2, 8, 34]
Hint
Use the keyword method for starting the List comprehension and fill in the relevant parts.

Even numbers can be divided by 2 with no remainder.

Remind yourself of how the modulo operator works."""
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
def FilterEvenNumbers(numbers):
    """
    Take a list of numbers, filter even numbers and return a list.-
    """
    return [n for n in numbers if ((n % 2) == 0)]


#
# main
#
if __name__ == "__main__":
    # Clear console
    clear_console()


#
# Test
#


# Import
import unittest

# Create tests
class MyTest(unittest.TestCase):
    # test_1
    def test_1(self):
        filtered = FilterEvenNumbers(range(1, 10))
        self.assertEqual([2, 4, 6, 8], filtered)


# Run tests
print("\n")
print("Running some tests on the code:")
print(".\n.\n.\n.")
unittest.main(verbosity=1, exit=False)