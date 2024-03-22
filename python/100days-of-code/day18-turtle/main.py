import turtle
from random import *

turtle.colormode(255)
timmy = turtle.Turtle()
timmy.shape("turtle")
timmy.color("red")

#for i in range(20):
#    timmy.pendown()
#    timmy.forward(10)
#    timmy.penup()
#    timmy.forward(10)
turn = [ 30, 45, 60, 90 ]
length = [20, 40, 60]
direction = ["right", "left"]
timmy.pensize(1)
timmy.speed("fastest")


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return(r, g, b)


#for i in range(50):
#    tup = (random_color())
#    timmy.pencolor(tup)
#    dir = choice(direction)
#    if dir == "right":
#        timmy.right(choice(turn))
#    else:
#        timmy.left(choice(turn))
#    timmy.forward(choice(length))

for i in range(120):
    timmy.color(randint(0, 255), randint(0, 255), randint(0, 255))
    timmy.circle(100)
    timmy.left(3)




screen = turtle.Screen()
screen.exitonclick()