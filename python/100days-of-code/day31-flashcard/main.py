from tkinter import *
import pandas
from random import randint

BACKGROUND_COLOR = "#B1DDC6"
eng = ""
esp = ""

try: 
    data = pandas.read_csv("data/words_to_learn.csv") 
    data_dict = data.to_dict(orient="records")
except: 
    data = pandas.read_csv("data/spanish_words.csv") 
    data_dict = data.to_dict(orient="records")

# random selecting a card
def nextcard():
    global eng, esp
    index = randint(0, len(data_dict)-1)
    eng = data_dict[index]["EN"]
    esp = data_dict[index]["ES"]
    canvas.itemconfig(canvas_image, image=frontimage)
    canvas.itemconfig(card_title, text="Spanish", fill="black")
    canvas.itemconfig(card_word, text=esp, fill="black")
    window.after(3000, flipcard)

# flip the card
def flipcard(): 
    canvas.itemconfig(canvas_image, image=backimage)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=eng, fill="white")

def greenflow():
    data_dict.remove({'ES': esp, 'EN': eng})
    print(len(data_dict))
    export = pandas.DataFrame.from_records(data_dict)
    export.to_csv("data/words_to_learn.csv", index=False)
    nextcard()

# GUI setup
window = Tk()
window.title("FlashCard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
frontimage=PhotoImage(file="images/card_front.png")
backimage=PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=frontimage)
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(400, 150, text = "Spanish", font = ("Arial", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text = "word", font = ("Arial", 60, "bold"), fill="black")

redno = PhotoImage(file="images/wrong.png")
no = Button(image=redno, highlightthickness=0, command=nextcard)
no.grid(row=1, column=0)

greenyes = PhotoImage(file="images/right.png")
yes = Button(image=greenyes, highlightthickness=0, command=greenflow)
yes.grid(row=1, column=1)

nextcard()


window.mainloop()

