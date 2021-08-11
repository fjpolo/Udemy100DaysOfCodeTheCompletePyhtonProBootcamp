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
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


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
    window.title("My First GUI Program")
    window.minsize(width=500, height=300)
    window.config(padx=100, pady=200)

    # Label
    my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
    my_label.config(text="New Text")
    my_label.grid(column=0, row=0)
    my_label.config(padx=50, pady=50)

    # Button
    button = Button(text="Click Me", command=button_clicked)
    button.grid(column=1, row=1)

    new_button = Button(text="New Button")
    new_button.grid(column=2, row=0)

    # Entry
    input = Entry(width=10)
    print(input.get())
    input.grid(column=3, row=2)

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