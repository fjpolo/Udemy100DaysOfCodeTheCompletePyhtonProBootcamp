import os
from turtle import Turtle

#
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

#
def read_highscore():
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )
    with open(os.path.join(__location__, "data.txt"), mode="r") as file:
        return int(file.read())


#
def write_highscore(highscore):
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )
    with open(os.path.join(__location__, "data.txt"), mode="w") as file:
        file.write(highscore)


#
#
#
class Scoreboard(Turtle):
    def __init__(self):
        """
        Constructor.-
        """
        super().__init__()
        self.score = read_highscore()
        self.highscore = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=270)
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Updates scoreboard.-
        """
        self.clear()
        self.write(
            f"Score: {self.score} | High Score: {self.highscore}",
            align=ALIGNMENT,
            font=FONT,
        )

    def increase_score(self):
        """
        Increase score by one.-
        """
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        """
        Reset method.-
        """
        if self.score > self.highscore:
            self.highscore = self.score
            write_highscore(f"{self.highscore}")
        # reset score
        self.score = 0
        # update scoredboard
        self.update_scoreboard()

    # def game_over(self):
    #     """
    #     Game Over.-
    #     """
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)