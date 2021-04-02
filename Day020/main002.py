#
# Imports
#
import os
from turtle import Screen
import time
from snake import Snake


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
    command = "clear"
    if os.name in ("nt", "dos"):  # If Machine is running on Windows, use cls
        command = "cls"
    os.system(command)


#
# main
#
if __name__ == "__main__":
    # Clear console
    clear_console()

    #
    # Screen
    #

    # Create Screen
    screen = Screen()
    # Configure Height and Width
    screen.setup(width=600, height=600)
    # Configure backgroud colour
    screen.bgcolor("black")
    # Configure window title
    screen.title("Snakey")

    #
    # Snake
    #
    snakey = Snake()
    game_is_on = True

    #
    # Loop
    #
    while game_is_on:
        # Update graphics
        screen.update()
        # Delay
        time.sleep(0.1)
        # Move snake
        snakey.move()

    # Exit screen
    screen.exitonclick()
