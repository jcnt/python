from turtle import Turtle
from random import choice, randint

COLOR = ["red", "blue", "green", "grey", "black", "purple", "yellow", "orange"]
SPEED = 5
SPEEDUP = 3

class Cars(Turtle):
    def __init__(self):

        self.cars = []
        self.current_speed = SPEED

    def create_car(self):
        slowdown = randint(1, 6)
        if slowdown == 5:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(choice(COLOR))
            new_car.penup()
            rand_y = randint(-250, 250)
            new_car.goto(290, rand_y)
            self.cars.append(new_car)

    def move(self):
        for i in self.cars:
            i.backward(self.current_speed)

    def levelup(self):
        self.current_speed += SPEEDUP