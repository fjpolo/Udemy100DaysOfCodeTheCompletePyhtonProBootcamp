#
# Imports
#
import os
from turtle import Turtle, Screen
import pandas as pd
import tkinter

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
# main
#
if __name__ == "__main__":
    # Clear console
    clear_console()

    #
    # Hello GUI
    #

    # New window object
    window = tkinter.Tk()
    # Title
    window.title("Hallo Dikka")
    # Minimum size
    window.minsize(width=480, height=240)
    # New label
    my_label = tkinter.Label(text="I am a label Brüdi", font=("Arial", 24, "bold"))
    # my_label.pack()
    # my_label.pack(side="bottom")
    # my_label.pack(side="top")
    # my_label.pack(side="left")
    # my_label.pack(side="right")
    my_label.pack(expand=True)

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