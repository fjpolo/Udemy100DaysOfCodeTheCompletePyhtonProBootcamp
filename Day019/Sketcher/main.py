
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

#move_forward
def move_forward():
    """
    Moves timmy 10 steps forward.-
    """
    timmy.forward(10)

# move_backward
def move_backward():
    """
    Moves timmy 10 steps backward.-
    """
    timmy.backward(10)
# rotate_clockwise
def rotate_clockwise():
    """
    Rotates timmy 10° clockwise.-
    """
    timmy.setheading(timmy.heading() + 10)

# rotate_anticlockwise
def rotate_anticlockwise():
    """
    Rotates timmy 10° anticlockwise.-
    """
    timmy.setheading(timmy.heading() - 10)

# clear_drawing
def clear_drawing():
    """
    Clears drawing and centers timmy.-
    """
    timmy.penup()
    timmy.clear()
    timmy.home()
    timmy.pendown()


#
# main
#
if __name__ == "__main__":
    # Clear console
    clear_console()

    # Create timmy
    timmy = Turtle()
    timmy.speed(0)

    # Create screen
    screen = Screen()
    screen.listen()
    #
    screen.onkey(key='w', fun=move_forward)
    screen.onkey(key='s', fun=move_backward)
    screen.onkey(key='a', fun=rotate_clockwise)
    screen.onkey(key='d', fun=rotate_anticlockwise)
    screen.onkey(key='c', fun=clear_drawing)
    
    
    # Exit on click
    screen.exitonclick()
