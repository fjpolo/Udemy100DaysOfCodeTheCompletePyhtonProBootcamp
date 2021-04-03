from turtle import Turtle

#
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

#
#
#
class Scoreboard(Turtle):
    def __init__(self):
        """
        Constructor.-
        """
        super().__init__()
        self.score = 0
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
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """
        Increase score by one.-
        """
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        """
        Game Over.-
        """
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)