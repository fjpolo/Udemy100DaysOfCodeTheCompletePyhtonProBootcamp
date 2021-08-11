"""
Dictionary Comprehension 1
Instructions
You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the given sentence and calculates the number of letters in each word.

Try Googling to find out how to convert a sentence into a list of words.

Do NOT Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.

Example Output
{
'What': 4, 
'is': 2, 
'the': 3, 
'Airspeed': 8, 
'Velocity': 8, 
'of': 2, 
'an': 2, 
'Unladen': 7, 
'Swallow?': 8
}
Hint
Use the keyword method for starting the Dictionary comprehension and fill in the relevant parts.

You can get a list of the words in a string by using the .split() method: https://www.w3schools.com/python/ref_string_split.asp
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


# Incomprendido
def Incomprendido(sentence):
    """
    Takes each word in the given sentence and calculates the number of letters in each word.-
    """
    return {word: len(word) for word in sentence.split()}


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
        result = Incomprendido("What is the Airspeed Velocity of an Unladen Swallow?")
        self.assertEqual(
            {
                "Airspeed": 8,
                "Swallow?": 8,
                "Unladen": 7,
                "Velocity": 8,
                "What": 4,
                "an": 2,
                "is": 2,
                "of": 2,
                "the": 3,
            },
            result,
        )


# Run tests
print("\n")
print("Running some tests on the code:")
print(".\n.\n.\n.")
unittest.main(verbosity=1, exit=False)