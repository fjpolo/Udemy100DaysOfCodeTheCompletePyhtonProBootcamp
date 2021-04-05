#
# Imports
#
import os
from turtle import Turtle, Screen
from paddle import Paddle

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
    # Variables
    #
    game_is_on = True

    #
    # Screen
    #
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.title("Pong")
    screen.tracer(False)

    #
    # Paddles
    #
    r_paddle = Paddle((350, 0))
    l_paddle = Paddle((-350, 0))

    #
    # Move paddles
    #
    screen.listen()
    screen.onkey(r_paddle.go_up, "Up")
    screen.onkey(r_paddle.go_dn, "Down")
    screen.onkey(l_paddle.go_up, "w")
    screen.onkey(l_paddle.go_dn, "s")

    # While game on
    while game_is_on:
        screen.update()

    # Screen: exit on click
    screen.exitonclick()