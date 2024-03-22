import turtle
import csv

screen = turtle.Screen()
screen.title("U.S. Stage Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

stprint = turtle.Turtle()
stprint.penup()
stprint.ht()

# this is how you would get the coordinates with clicking on the screen -> into CSV
#def get_mouse_click_coor(x, y): 
#    print(x, y)
#turtle.onscreenclick(get_mouse_click_coor)

states = []
progress =[]

with open("50_states.csv") as file: 
    data = csv.reader(file)
    for i in range(51):
        i = file.readline().split(",")
        states.append(i)

def fillup():
    ycor2 = 250
    for j in range(1,51):
        xcor2 = -350
        if states[j][0] not in progress: 
            stprint.goto(xcor2, ycor2)
            stprint.write(states[j][0], align="center", font=("Arial", 12, "italic"))
            ycor2 -= 15

running = True
while running:
    if len(progress) < 50: 
        answer_state = screen.textinput(title=f"{len(progress)}/50 Name the States", prompt="Name a State")
    tstate = answer_state.title()
    if tstate == "Giveup":
        fillup()
    for i in range(51): 
        if tstate == states[i][0]: 
            xcor = int(states[i][1])
            ycor = int(states[i][2])
            stprint.goto(xcor, ycor)
            stprint.write(tstate, align="center", font=("Arial", 12, "normal"))
            if tstate not in progress: 
                progress.append(tstate)

turtle.mainloop()

