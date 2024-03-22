from turtle import Screen
from player import Player
from time import sleep
from cars import Cars
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("white")
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
cars = Cars()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "space")

on = True

while on:
    sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move()

    # detect collision with cars
    for i in cars.cars:
        if i.distance(player) < 15:
            scoreboard.update_highscore()
            on = False

    # detect when player crossed the street
    if player.ycor() == 280:
        player.goto(0, -280)
        scoreboard.increase_score()
        cars.levelup()

screen.exitonclick()