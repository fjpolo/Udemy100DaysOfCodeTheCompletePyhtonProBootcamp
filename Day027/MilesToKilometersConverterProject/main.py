#
# Imports
#
import os
from turtle import Turtle, Screen
import pandas as pd
from tkinter import *

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


# button_clicked
def calculate_button_clicked():
    km = int(miles_input.get()) * 1.609
    result_km_label.config(text=km)


#
# main
#
if __name__ == "__main__":
    # Clear console
    clear_console()

    #
    # Hello GUI
    #

    # Window
    window = Tk()
    window.title("Miles to Kilometers converter")
    window.minsize()

    # Entry
    miles_input = Entry(width=10)
    miles_input.grid(column=1, row=0)

    # Labels
    miles_label = Label(text="Miles")
    miles_label.grid(column=2, row=0)
    result_km_label = Label(text="0")
    result_km_label.grid(column=1, row=1)
    km_label = Label(text="Km")
    km_label.grid(column=2, row=1)
    is_equal_label = Label(text="is equal to")
    is_equal_label.grid(column=0, row=1)

    # Button
    calculate_button = Button(text="Calculate", command=calculate_button_clicked)
    calculate_button.grid(column=1, row=2)

    # Show window
    window.mainloop()


#
# Test
#


# # Import
# import unittest

# # Create tests
# class MyTest(unittest.TestCase):
#     # test_1
#     def test_1(self):
#         result = FUT(parameter)
#         self.assertEqual(
#             expected_result,
#             result,
#         )


# # Run tests
# print("\n")
# print("Running some tests on the code:")
# print(".\n.\n.\n.")
# unittest.main(verbosity=1, exit=False)