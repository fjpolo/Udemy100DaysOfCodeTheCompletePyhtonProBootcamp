#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp





#
# Imports
#
import os
from turtle import Turtle, Screen

#
# Classes
#

#
# Global variables
#
PLACEHOLDER = "[name]"

#
# Private functions
#

# clear_console
def clear_console():
    """
    Clears console.
    """
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


#
# main
#
if __name__ == "__main__":
    # Clear console
    clear_console()

    # Read names
    with open("Input/Names/invited_names.txt") as names_file:
        names = names_file.readlines()
    
    # Open template letter
    with open("Input/Letters/starting_letter.txt") as letter_file:
        letter_contents = letter_file.read()
        # Replace placeholder
        for name in names:
            new_letter = letter_contents.replace(PLACEHOLDER, name.strip())
            # Save letter
            with open(f"Output/ReadyToSend/letter_for_{name.strip()}.txt", mode="w") as completed_letter:
                completed_letter.write(new_letter)

