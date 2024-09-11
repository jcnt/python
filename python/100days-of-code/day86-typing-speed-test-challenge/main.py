# assignment program for python GUI
# Day 85: write a GUI program to test typing speed of the player
#
import random as rnd
import time
import tkinter as tk

time_sec = 60
chcounter = 0


def get_text():
    with open("alice_in_wonderland.txt") as text:
        lines = text.readlines()
        text = ""
        start = rnd.randint(1, 180)
        for _ in range(20):
            text += lines[start]
            start += 1
        text = text.lower()
        return text


def count_down(count):
    global chcounter
    time_label.config(text=f"Time remaining: {count} sec")
    if count > 0:
        window.after(1000, count_down, count - 1)
        chcounter = len(typespace.get("1.0", "end-1c"))
        char_label.config(text=f"Characters: {chcounter}")
    else:
        text_label.config(
            text=f"Congratulations!\nYou typed {chcounter} characters in 60 seconds! ",
            font=("Arial", 14, "bold"),
        )


def game_start():
    in_text = get_text()
    text_label.config(text=in_text)
    typespace.delete(1.0, tk.END)
    count_down(time_sec)


window = tk.Tk()
window.title("Typing Speed Tester")
window.minsize(height=700, width=1000)
window.config(padx=50, pady=50)


text_label = tk.Label(
    text="Rules: Simple, click on START and you'll get a text. You have 60 seconds. Type as much as you can!",
    width=100,
    height=25,
)

text_label.grid(row=0, column=0, columnspan=3)

typespace = tk.Text(width=100, height=20)
typespace.focus_set()
typespace.grid(row=1, column=0, columnspan=3)

char_label = tk.Label(text=f"Characters: {chcounter}")
char_label.grid(row=2, column=0)

start = tk.Button(text="START", command=game_start)
start.grid(row=2, column=1)

time_label = tk.Label(text=f"Time remaining: {time_sec} sec")
time_label.grid(row=2, column=2)

window.mainloop()
