
#
# Imports
#
import os
from turtle import Turtle, Screen
import random

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
    # Create Timmy
    timmy = Turtle()
    timmy.shape("turtle")
    # Create screen
    screen = Screen()
    screen.colormode(255)

    # Iterate from triangle to decagon
    for it in range(3, 11):
        # Change colour
        timmy.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        # Calculate angle
        angle = float(360/it)
        # loop and draw
        for _ in range(it):
            timmy.forward(100)
            timmy.right(angle)


    #
    screen.exitonclick()