"""
List Comprehension 3
💪 This exercise is HARD

Instructions
Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.

You are going to create a list called result which contains the numbers that are common in both files.

e.g. if file1.txt contained:

1
2
3
and file2.txt contained:

2
3
4
result = [2, 3]
IMPORTANT: The result should be a list that contains Integers, not Strings. Try to use List Comprehension instead of a Loop.

Example Output
[3, 6, 5, 33, 12, 7, 42, 13]
Hint
Use the keyword method for starting the List comprehension and fill in the relevant parts.

First, you will need to read from the files and create a list using the lines in the files.

This method will be really useful: https://www.w3schools.com/python/ref_file_readlines.asp

Remember you can check if a value exists in a list using the in keyword. https://www.w3schools.com/python/ref_keyword_in.asp

Remember you can convert a string to an int using the int() method. https://www.w3schools.com/python/ref_func_int.asp
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


# DataOverlap
def DataOverlap(list1, list2):
    """
    Takes two lists and returns a list of common numbers.-
    """
    return [int(n) for n in list1 if (n in list2)]


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
        list_file1 = [1, 2, 3]
        list_file2 = [2, 3, 4]
        result = DataOverlap(list_file1, list_file2)
        self.assertEqual([2, 3], result)

    # test_2
    def test_2(self):
        with open("file1.txt") as file1:
            list_file1 = file1.readlines()
        with open("file2.txt") as file2:
            list_file2 = file2.readlines()
        result = DataOverlap(list_file1, list_file2)
        self.assertEqual([3, 6, 5, 33, 12, 7, 42, 13], result)


# Run tests
print("\n")
print("Running some tests on the code:")
print(".\n.\n.\n.")
unittest.main(verbosity=1, exit=False)