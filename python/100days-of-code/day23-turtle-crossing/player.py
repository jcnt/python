from turtle import Turtle

STARTPOS = (0, -280)
MOVE = 10

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.penup()
        self.goto(STARTPOS)

    def move(self):
        self.forward(MOVE)
