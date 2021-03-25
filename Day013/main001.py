
#
# Imports
#
import os
from random import randint

#
# Global variables
#


#
# Private functions
#

# clearConsole
def clearConsole():
    """
    Clears console.
    """
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

# my_function
def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")

# mutate
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)
#
# main
#
if __name__ == "__main__":
    clearConsole()

    # Describe Problem
    print("Describe Problem")
    my_function()
    print('\n')

    # Reproduce the Bug
    print("Reproduce the Bug")
    my_function()
    dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
    dice_num = randint(0, 5)
    print(dice_imgs[dice_num])
    print('\n')

    # Play Computer
    print("Play Computer")
    year = int(input("What's your year of birth?"))
    if year > 1980 and year < 1994:
      print("You are a millenial.")
    elif year >= 1994:
      print("You are a Gen Z.")
    print('\n')

    # Fix the Errors
    print("Fix the Errors")
    age = int(input("How old are you?"))
    if age >= 18:
        print("You can drive at age {age}.")
    print('\n')

    #Print is Your Friend
    print("Print is Your Friend")
    pages = 0
    word_per_page = 0
    pages = int(input("Number of pages: "))
    word_per_page = int(input("Number of words per page: "))
    total_words = pages * word_per_page
    print(total_words)
    print('\n')

    #Use a Debugger
    print("Use a Debugger")
    mutate([1,2,3,5,8,13])
    print('\n')

