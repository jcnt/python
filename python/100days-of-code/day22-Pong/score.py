from turtle import Turtle

FONT = ("Arial", 24, "normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()

        self.lscore = 0
        self.rscore = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.lscore} : {self.rscore}", align="center", font=FONT)

    def score_left(self):
        self.lscore += 1
        self.clear()
        self.update_score()

    def score_right(self):
        self.rscore += 1
        self.clear()
        self.update_score()
