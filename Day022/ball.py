from turtle import Turtle
import time

#
# Class Ball
#
class Ball(Turtle):
    def __init__(self):
        """
        Class constructor.-
        """
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.moving_speed = 0.1

    def move(self):
        """
        Moves the ball.-
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def bounce_y(self):
        """
        Bounces the ball on y axis.-
        """
        self.y_move *= -1

    def bounce_x(self):
        """
        Bounces the ball on x axis.-
        """
        self.x_move *= -1
        self.moving_speed *= 0.9

    def reset(self):
        """
        Resets ball to centre.-
        """
        self.goto(0, 0)
        self.bounce_x()
        # time.sleep(2)
        self.moving_speed = 0.1
