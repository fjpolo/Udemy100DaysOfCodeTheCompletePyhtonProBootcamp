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
    command = "clear"
    if os.name in ("nt", "dos"):  # If Machine is running on Windows, use cls
        command = "cls"
    os.system(command)


#
def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


#
def go_dn():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)


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
    # Paddle
    #
    paddle = Turtle()
    paddle.shape("square")
    paddle.color("white")
    paddle.shapesize(stretch_wid=5, stretch_len=1)
    paddle.penup()
    paddle.goto(x=350, y=0)

    #
    # Move paddle
    #
    screen.listen()
    screen.onkey(go_up, "Up")
    screen.onkey(go_dn, "Down")

    # While game on
    while game_is_on:
        screen.update()

    # Screen: exit on click
    screen.exitonclick()