"""
Dictionary Comprehension 2
Instructions
You are going to use Dictionary Comprehension to create a dictionary called weather_f that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.

To convert temp_c into temp_f:
(temp_c * 9/5) + 32 = temp_f
Do NOT Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.

Example Output
{
'Monday': 53.6, 
'Tuesday': 57.2, 
'Wednesday': 59.0, 
'Thursday': 57.2, 
'Friday': 69.8, 
'Saturday': 71.6, 
'Sunday': 75.2
}
Hint
Use the keyword method for starting the Dictionary comprehension and fill in the relevant parts.

You can get each of the items from a dictionary using the .items() method: https://www.w3schools.com/python/ref_dictionary_items.asp
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
def Incomprendido(weather_c):
    """
    Convert °C temp to worldwide unused F.-
    """
    return {day: (temp_c * 9 / 5) + 32 for (day, temp_c) in weather_c.items()}


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
        weather_c = {
            "Monday": 12,
            "Tuesday": 14,
            "Wednesday": 15,
            "Thursday": 14,
            "Friday": 21,
            "Saturday": 22,
            "Sunday": 24,
        }
        weather_f = Incomprendido(weather_c)
        self.assertEqual(
            {
                "Monday": 53.6,
                "Tuesday": 57.2,
                "Wednesday": 59.0,
                "Thursday": 57.2,
                "Friday": 69.8,
                "Saturday": 71.6,
                "Sunday": 75.2,
            },
            weather_f,
        )


# Run tests
print("\n")
print("Running some tests on the code:")
print(".\n.\n.\n.")
unittest.main(verbosity=1, exit=False)