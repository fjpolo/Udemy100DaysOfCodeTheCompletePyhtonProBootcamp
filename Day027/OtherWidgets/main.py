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


# action
def action():
    print("Do something")


# spinbox_used
def spinbox_used():
    # gets the current value in spinbox.
    print(spinbox.get())


# scale_used
def scale_used(value):
    print(value)


# checkbutton_used
def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())


# radio_used
def radio_used():
    print(radio_state.get())


# listbox_used
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


#
# main
#
if __name__ == "__main__":
    # Clear console
    clear_console()

    # Creating a new window and configurations
    window = Tk()
    window.title("Widget Examples")
    window.minsize(width=500, height=500)

    # Labels
    label = Label(text="This is old text")
    label.config(text="This is new text")
    label.pack()

    # Buttons
    # calls action() when pressed
    button = Button(text="Click Me", command=action)
    button.pack()

    # Entries
    entry = Entry(width=30)
    # Add some text to begin with
    entry.insert(END, string="Some text to begin with.")
    # Gets text in entry
    print(entry.get())
    entry.pack()

    # Text
    text = Text(height=5, width=30)
    # Puts cursor in textbox.
    text.focus()
    # Adds some text to begin with.
    text.insert(END, "Example of multi-line text entry.")
    # Get's current value in textbox at line 1, character 0
    print(text.get("1.0", END))
    text.pack()

    # Spinbox
    spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
    spinbox.pack()

    # Scale
    # Called with current scale value.
    scale = Scale(from_=0, to=100, command=scale_used)
    scale.pack()

    # Checkbutton
    # variable to hold on to checked state, 0 is off, 1 is on.
    checked_state = IntVar()
    checkbutton = Checkbutton(
        text="Is On?", variable=checked_state, command=checkbutton_used
    )
    checked_state.get()
    checkbutton.pack()

    # Radiobutton
    # Variable to hold on to which radio button value is checked.
    radio_state = IntVar()
    radiobutton1 = Radiobutton(
        text="Option1", value=1, variable=radio_state, command=radio_used
    )
    radiobutton2 = Radiobutton(
        text="Option2", value=2, variable=radio_state, command=radio_used
    )
    radiobutton1.pack()
    radiobutton2.pack()

    # Listbox
    listbox = Listbox(height=4)
    fruits = ["Apple", "Pear", "Orange", "Banana"]
    for item in fruits:
        listbox.insert(fruits.index(item), item)
    listbox.bind("<<ListboxSelect>>", listbox_used)
    listbox.pack()
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