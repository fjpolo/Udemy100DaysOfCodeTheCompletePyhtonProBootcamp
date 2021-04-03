from turtle import Turtle, Screen
import random

#
#
#
class Food(Turtle):
    def __init__(self):
        """
        Constructor.-
        """
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("green")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """
        Refresh food location.-
        """
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(x=random_x, y=random_y)
