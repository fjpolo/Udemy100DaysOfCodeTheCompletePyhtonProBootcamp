
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
directions = [0, 90, 180, 270]

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
    # make it THICC
    timmy.pensize(10)
    # speed
    timmy.speed(10)

    # Create screen
    screen = Screen()
    screen.colormode(255)

    for _ in range(200):
        # Change colour
        timmy.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        # Random walk
        timmy.forward(50) 
        # Turn
        timmy.setheading(random.choice(directions))   


    #
    screen.exitonclick()