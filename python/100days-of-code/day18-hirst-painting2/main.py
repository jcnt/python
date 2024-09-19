import random
import turtle

import colorgram

turtle.colormode(255)
tim = turtle.Turtle()

tim.penup()
tim.setpos(-300, -50)
tim.pendown()

colorlist = [
    (84, 254, 155),
    (173, 146, 118),
    (254, 250, 254),
    (245, 39, 191),
    (158, 107, 56),
    (2, 1, 176),
    (151, 54, 251),
    (221, 254, 101),
    (253, 146, 193),
    (3, 87, 176),
    (249, 1, 246),
    (35, 34, 253),
    (1, 213, 212),
    (249, 0, 0),
    (254, 147, 146),
    (253, 71, 70),
    (244, 248, 254),
    (39, 249, 42),
]


# colors = colorgram.extract("image.jpg", 20)

# colorlist = []
#
# for i in range(20):
#    act_color = colors[i]
#    r = act_color.rgb.r
#    g = act_color.rgb.g
#    b = act_color.rgb.b
#    rgb = (r, g, b)
#    colorlist.append(rgb)

# print(colorlist)
#
# tim.pensize(50)
#
# for j in range(6):
#    tim.pendown()
#    tim.color(colorlist[j])
#    tim.forward(50)
#    tim.penup()
#    tim.forward(25)

collen = len(colorlist)
tim.pensize(20)

for i in range(10):
    for j in range(10):
        act_num = random.randint(0, collen - 1)
        act_color = colorlist[act_num]
        tim.color(act_color)
        tim.pendown()
        tim.forward(1)
        tim.penup()
        tim.forward(50)
    tim.goto(-300, i * 50)

tim.hideturtle()

screen = turtle.Screen()
screen.exitonclick()
