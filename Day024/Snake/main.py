#
# Imports
#
import os
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

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
    screen.tracer(0)

    #
    # Snake
    #
    snakey = Snake()
    # Listen...
    screen.listen()
    screen.onkey(snakey.up, "Up")
    screen.onkey(snakey.down, "Down")
    screen.onkey(snakey.left, "Left")
    screen.onkey(snakey.right, "Right")

    #
    # Food
    #
    food = Food()

    #
    # Scoreboard
    #
    score = Scoreboard()

    # game_is_on flag
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
        # Collission with food
        if snakey.head.distance(food) < 15:
            snakey.extend()
            score.increase_score()
            food.refresh()
        # Collission with wall
        if (
            snakey.head.xcor() > 280
            or snakey.head.xcor() < -280
            or snakey.head.ycor() > 280
            or snakey.head.ycor() < -280
        ):
            # Game over
            # game_is_on = False
            # score.game_over()
            score.reset()
            snakey.reset()

        # Collission with tail
        for segment in snakey.segments[1::1]:
            if snakey.head.distance(segment) < 10:
                # Game Over
                # game_is_on = False
                # Game Over
                # score.game_over()
                score.reset()
                snakey.reset()

    # Exit screen
    screen.exitonclick()
