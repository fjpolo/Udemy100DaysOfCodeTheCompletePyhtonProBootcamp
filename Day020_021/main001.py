#
# Imports
#
import os
from turtle import Turtle, Screen
import time

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
    game_is_on = True

    # Step 1: Create three turtles being squares, that's the snake

    # Hard way:
    # segment_1 = Turtle("square")
    # segment_1.color("white")
    # segment_2 = Turtle("square")
    # segment_2.color("white")
    # segment_2.goto(x=-20, y=0)
    # segment_3 = Turtle("square")
    # segment_3.color("white")
    # segment_3.goto(x=-40, y=0)

    # Easy way
    for position in starting_positions:
        # Create turtle
        new_segment = Turtle("square")
        # Change colour
        new_segment.color("white")
        # Pen up
        new_segment.penup()
        # Move turtle
        new_segment.goto(position)
        # Add to turtles list
        segments.append(new_segment)

    while game_is_on:
        # Update graphics
        screen.update()
        # Delay
        time.sleep(0.1)
        # Step 2: Move our snakey forward
        # for seg_num in range(start=2, stop=0, range=-1):
        for seg_num in range(len(segments) - 1, 0, -1):
            # Replace second to last segment with last segment
            segments[seg_num].goto(
                segments[seg_num - 1].xcor(), segments[seg_num - 1].ycor()
            )
        # Move first segment
        segments[0].forward(20)

    # Exit screen
    screen.exitonclick()
