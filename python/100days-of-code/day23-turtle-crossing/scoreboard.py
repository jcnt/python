from turtle import Turtle

FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.score = 0
        with open("highscore") as file:
            self.highscore = int(file.read())
        self.color("black")
        self.penup()
        self.goto(160, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}, High score: {self.highscore}", align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_highscore(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore", mode="w") as file:
                file.write(f"{self.highscore}")
