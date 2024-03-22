from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from time import sleep
from score import Score

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

left = Paddle(-380)
right = Paddle(370)
ball = Ball()
score = Score()

screen.listen()
screen.onkey(left.go_up, "s")
screen.onkey(left.go_down, "x")
screen.onkey(right.go_up, "Up")
screen.onkey(right.go_down, "Down")

sl = 0.1
running = True

while running:
    sleep(sl)
    screen.update()
    ball.move()
    score

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bouncey()

    # detect collision with ends
    if ball.distance(right) < 50 and ball.xcor() > 340:
        ball.bouncex()
        sl /= 1.2

    if ball.distance(left) < 50 and ball.xcor() < -340:
        ball.bouncex()
        sl /= 1.2

    # detect ball going out right
    if ball.xcor() > 390:
        ball.resetpos()
        ball.move()
        score.score_left()
        sl = 0.1
        if score.lscore == 5:
            running = False

    # detect ball going out left
    if ball.xcor() < -390:
        ball.resetpos()
        ball.move()
        score.score_right()
        sl = 0.1
        if score.rscore == 5:
            running = False

screen.exitonclick()
