from math import floor
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
currchecked = []
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def timereset():
    global reps
    reps = 0
    global currchecked
    window.after_cancel(timer)
    maintitle.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    currchecked = []
    checked.config(text=currchecked)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def timestart():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # Tester timer with short times
    #    work_sec = 8
    #    short_break_sec = 2
    #    long_break_sec = 7

    #   original idea, but instructor's code is cleaner, see below
    #
    #    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
    #        count_down(work_sec)
    #        currchecked.append("✔")
    #    elif reps == 2 or reps == 4 or reps == 6:
    #        count_down(short_break_sec)
    #    elif reps == 8:
    #        count_down(long_break_sec)
    #        reps = 0

    if reps % 8 == 0:
        count_down(long_break_sec)
        maintitle.config(text="Break", fg=RED)
        reps = 0
    elif reps % 2 == 0:
        count_down(short_break_sec)
        maintitle.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        maintitle.config(text="Working", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global currchecked
    count_min = floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        timestart()
        if len(currchecked) == 4:
            currchecked = []
            checked.config(text=currchecked)
        if reps % 2 == 0:
            currchecked.append("✔")
            checked.config(text=currchecked)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomatoimg = PhotoImage(file="tomato.png")
canvas.create_image(
    100, 112, image=tomatoimg
)  # 100, 112 is the position on canvas (center)
timer_text = canvas.create_text(
    103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(row=1, column=1)

start = Button(text="Start", highlightthickness=0, command=timestart)
start.grid(row=2, column=0)
start.config(bg=YELLOW)

reset = Button(text="reset", highlightthickness=0, command=timereset)
reset.grid(row=2, column=2)

checked = Label(text=currchecked, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 18, "normal"))
checked.grid(row=3, column=1)

maintitle = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "normal"))
maintitle.grid(row=0, column=1)


window.mainloop()
