
#
# Imports
#
import os
from turtle import Turtle, Screen
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
    clear_console()
    
    # Create Jaimito turtle
    jaimito = Turtle()
    # Print object
    print(jaimito)
    jaimito.shape("turtle")
    jaimito.color("blue")
    jaimito.speed(7)
    # Move forward
    jaimito.forward(100)
    # Create screen
    my_screen = Screen()
    print(my_screen.canvheight)
    print(my_screen.canvwidth)
    # Run program until click on screen
    my_screen.exitonclick()
    
