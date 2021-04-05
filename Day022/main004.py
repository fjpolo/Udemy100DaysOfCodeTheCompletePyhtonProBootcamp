#
# Imports
#
import os
import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball

#
# Constants
#
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 800
R_PADDLE_STARTING_POINT = (350, 0)
L_PADDLE_STARTING_POINT = (-350, 0)

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
    screen.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    screen.title("Pong")
    screen.tracer(0)

    #
    # Paddles
    #
    r_paddle = Paddle(R_PADDLE_STARTING_POINT)
    l_paddle = Paddle(L_PADDLE_STARTING_POINT)

    #
    # Ball
    #
    ball = Ball()

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
        time.sleep(0.1)
        ball.move()
        screen.update()

        # Collision with wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            # Bounce the ball
            ball.bounce_y()

        # Collision with paddle
        if (
            ball.distance(r_paddle) < 50
            and ball.xcor() > 320
            or ball.distance(l_paddle) < 50
            and ball.xcor() < -320
        ):
            ball.bounce_x()

    # Screen: exit on click
    screen.exitonclick()