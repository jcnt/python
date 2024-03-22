from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = "Make your bet.", prompt = "Which turtle will win the race?")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = -120
all_turtles = []

for i in colors:
    act_color = i
    i = Turtle(shape="turtle")
    i.color(act_color)
    i.penup()
    i.goto(x=-230, y=y_pos)
    y_pos += 50
    all_turtles.append(i)

game_on = True

while game_on:
    for j in all_turtles:
        act_move = randint(0, 10)
        j.forward(act_move)
        act_pos = j.pos()
        if act_pos[0] >= 250:
            winner = j.pencolor()
            if user_bet == winner:
                print(f"You guessed right, the {winner} has won!")
            else:
                print(f"You lose! The {winner} has won!")
            game_on = False


screen.exitonclick()
