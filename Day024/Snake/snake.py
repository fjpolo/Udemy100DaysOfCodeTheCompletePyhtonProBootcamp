# Imports
from turtle import Turtle, Screen

# Consts
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

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
        self.head = self.segments[0]

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
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """
        Head up.-
        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """
        Head down.-
        """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """
        Head left.-
        """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """
        Head right.-
        """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def add_segment(self, position):
        """
        Adds one segment.-
        """
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

    def extend(self):
        """
        Extend snake's length by one.-
        """
        # Extend one segment at tail
        self.add_segment(self.segments[-1].position())

    def reset(self):
        """
        Reset snake.-
        """
        for seg in self.segments:
            seg.goto(9999, 9999)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
