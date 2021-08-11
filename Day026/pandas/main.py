"""
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


# Pandita
def Pandita(df):
    """"""
    return {}


#
# main
#
if __name__ == "__main__":
    # Clear console
    clear_console()

    # For Loop
    numbers = [1, 2, 3]
    new_list = []
    for n in numbers:
        add_1 = n + 1
        new_list.append(add_1)

    # List Comprehension
    new_list = [n + 1 for n in numbers]

    # String as List
    name = "Angela"
    letters_list = [letter for letter in name]

    # Range as List
    range_list = [n * 2 for n in range(1, 5)]

    # Conditional List Comprenhension
    names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
    short_names = [name for name in names if len(name) < 5]

    upper_case_names = [name.upper() for name in names if len(name) > 4]

    # Dictionary Comprehension
    import random

    student_grades = {name: random.randint(1, 100) for name in names}
    print(student_grades)

    passed_students = {
        student: grade for (student, grade) in student_grades.items() if grade >= 60
    }
    print(passed_students)

    # Pandas
    student_dict = {"student": ["Angela", "James", "Lily"], "score": [56, 76, 98]}
    student_df = pd.DataFrame(student_dict)
    for (key, value) in student_df.items():
        print(key)
        print(value)
    # Loop through rows of a DF
    for (index, row) in student_df.iterrows():
        # print(index)
        print(row.student)
        print(row.score)

#
# Test
#


# # Import
# import unittest

# # Create tests
# class MyTest(unittest.TestCase):
#     # test_1
#     def test_1(self):

#         result = Pandita()
#         self.assertEqual(
#             {},
#             result,
#         )


# # Run tests
# print("\n")
# print("Running some tests on the code:")
# print(".\n.\n.\n.")
# unittest.main(verbosity=1, exit=False)