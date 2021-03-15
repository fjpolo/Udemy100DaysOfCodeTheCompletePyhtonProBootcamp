"""
Prime numbers are numbers that can only be cleanly divided by itself and 1.

https://en.wikipedia.org/wiki/Prime_number

You need to write a function that checks whether if the number passed into it is a prime number or not.

e.g. 2 is a prime number because it's only divisible by 1 and 2.

But 4 is not a prime number because you can divide it by 1, 2 or 4.

https://cdn.fs.teachablecdn.com/s0gceS97QD6MP5RUT49H

Here are the numbers up to 100, prime numbers are highlighted in yellow:

https://cdn.fs.teachablecdn.com/NZqVclSt2qAe8KhTsUtw

Example Input 1
73

Example Output 1
It's a prime number.

Example Input 2
75

Example Output 2
It's not a prime number.
"""
#
# Imports
#
import random

#
# Private functions
#

# prime_checker
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


#
# main
#
if __name__ == "__main__":
    #Do NOT change any of the code below👇
    n = int(input("Check this number: "))
    prime_checker(number=n)




# 
# Tests
#

# Imports
import unittest
from unittest.mock import patch
from io import StringIO

# Define tests
class MyTest(unittest.TestCase):
# Testing Print output
    def test_1(self): 
        with patch('sys.stdout', new = StringIO()) as fake_out: 
            prime_checker(87)
            expected_print = "It's not a prime number.\n"
            self.assertEqual(fake_out.getvalue(), expected_print) 

    def test_2(self): 
        with patch('sys.stdout', new = StringIO()) as fake_out: 
            prime_checker(97)
            expected_print = "It's a prime number.\n"
            self.assertEqual(fake_out.getvalue(), expected_print)

    def test_3(self): 
        with patch('sys.stdout', new = StringIO()) as fake_out: 
            prime_checker(66)
            expected_print = "It's not a prime number.\n"
            self.assertEqual(fake_out.getvalue(), expected_print)

    def test_4(self): 
        with patch('sys.stdout', new = StringIO()) as fake_out: 
            prime_checker(47)
            expected_print = "It's a prime number.\n"
            self.assertEqual(fake_out.getvalue(), expected_print)

# Ruin tests
print("\n")
print('Running some tests on your code:')
print(".\n.\n.\n.")
unittest.main(verbosity=1, exit=False)