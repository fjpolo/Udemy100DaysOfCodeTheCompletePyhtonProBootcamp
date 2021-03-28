
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

# random_colour
def random_colour():
    """ 
    Returns a random rgb thruple.-
    """
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# draw_spyrograph
def draw_spyrograph(gap_size):
    """
    Accepts a gap size and draws a spyrograph.-
    """
    for _ in range(int(360/gap_size)):
        # Spirograph
        timmy.color(random_colour())
        timmy.circle(100)
        # print(timmy.heading())
        timmy.setheading(timmy.heading() + gap_size)


#
# main
#
if __name__ == "__main__":
    # Clear console
    clear_console()
    # Create Timmy
    timmy = Turtle()
    timmy.shape("turtle")
    # fullspeed
    timmy.speed(0)

    # Create screen
    screen = Screen()
    screen.colormode(255)
    
    # Spyrograph
    draw_spyrograph(2)

    #
    screen.exitonclick()