"""
You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

number of cans = (wall height ✖️ wall width) ÷ coverage per can.

e.g. Height = 2, Width = 4, Coverage = 5

number of cans = (2 ✖️ 4) ÷ 5

                     = 1.6
                     = 1.6
But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.

IMPORTANT: Notice the name of the function and parameters must match those on line 13 for the code to work.
"""
#
# Imports
#
import random
import math

#
# Private functions
#
def paint_calc(height, width, cover):
    numberOfCans = math.ceil((height * width) / cover)
    print(f"You'll need {numberOfCans} cans of paint.")
    return numberOfCans


#
# main
#
if __name__ == "__main__":
    # Define a function called paint_calc() so that the code below works.   

    # 🚨 Don't change the code below 👇
    test_h = int(input("Height of wall: "))
    test_w = int(input("Width of wall: "))
    coverage = 5
    paint_calc(height=test_h, width=test_w, cover=coverage)



#
# Tests
#

# Import
import unittest
from unittest.mock import patch
from io import StringIO

# Create tests
class MyTest(unittest.TestCase):
# Testing Print output
    def test_1(self): 
        with patch('sys.stdout', new = StringIO()) as fake_out: 
            paint_calc(3, 6, 5)
            expected_print = "You'll need 4 cans of paint.\n"
            self.assertEqual(fake_out.getvalue(), expected_print) 

    def test_2(self): 
        with patch('sys.stdout', new = StringIO()) as fake_out: 
            paint_calc(3, 9, 5)
            expected_print = "You'll need 6 cans of paint.\n"
            self.assertEqual(fake_out.getvalue(), expected_print)

    def test_3(self): 
        with patch('sys.stdout', new = StringIO()) as fake_out: 
            paint_calc(7, 9, 2)
            expected_print = "You'll need 32 cans of paint.\n"
            self.assertEqual(fake_out.getvalue(), expected_print)

    def test_4(self): 
        with patch('sys.stdout', new = StringIO()) as fake_out: 
            paint_calc(12, 45, 5)
            expected_print = "You'll need 108 cans of paint.\n"
            self.assertEqual(fake_out.getvalue(), expected_print)

# Run tests
print("\n")
print('Running some tests on your code:')
print(".\n.\n.\n.")
unittest.main(verbosity=1, exit=False)