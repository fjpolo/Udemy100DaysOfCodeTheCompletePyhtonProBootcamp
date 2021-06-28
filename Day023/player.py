#
# Imports
#
from turtle import Turtle

#
# Constants
#
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
NORTH = 90
#
# Class Player
#
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.got_to_start()        
        self.setheading(NORTH)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_down(self):
        self.backward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        if self.ycor() > 280:
            return True
        else:
            return False
    
    def got_to_start(self):
        self.goto(STARTING_POSITION)