# Imports
from turtle import Turtle, Screen

# Consts
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

#
# Class Snake
#
class Snake:
    def __init__(self):
        """
        Snake Constructor.-
        """
        self.segments = []
        self.create_snake()

    def create_snake(self):
        """
        Creates a snake.-
        """
        for position in STARTING_POSITIONS:
            # Create turtle
            new_segment = Turtle("square")
            # Change colour
            new_segment.color("white")
            # Pen up
            new_segment.penup()
            # Move turtle
            new_segment.goto(position)
            # Add to turtles list
            self.segments.append(new_segment)

    def move(self):
        """
        Move snake forward.-
        """
        # Step 2: Move our snakey forward
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # Replace second to last segment with last segment
            self.segments[seg_num].goto(
                self.segments[seg_num - 1].xcor(), self.segments[seg_num - 1].ycor()
            )
        # Move first segment
        self.segments[0].forward(MOVE_DISTANCE)
