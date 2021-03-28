
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
    
    # Dashed line
    for _ in range(15):
        timmy.pendown()
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)


    # Create screen
    screen = Screen()
    screen.exitonclick()