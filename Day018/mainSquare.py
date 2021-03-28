
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
    timmy.color("blue")
    
    # Square
    # timmy.forward(100)
    # timmy.right(90)
    # timmy.forward(100)
    # timmy.right(90)
    # timmy.forward(100)
    # timmy.right(90)
    # timmy.forward(100)
    
    # Square
    for _ in range(4):
        timmy.forward(100)
        timmy.right(90)


    # Create screen
    screen = Screen()
    screen.exitonclick()