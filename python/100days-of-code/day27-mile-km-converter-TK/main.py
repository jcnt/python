from tkinter import * 

window = Tk()
window.title("Mile to Kilometer converter")
window.minsize(300, 150)
window.config(padx=5, pady=5)

to = 0
fromtxt = "Miles"
totxt = "Km"

radio_state = IntVar()

def milestokm():
    fromval = float(input.get())
    to = fromval * 1.6
    outcome.config(text=to)

def kmtomiles():
    fromval = float(input.get())
    to = fromval / 1.6
    outcome.config(text=to)

def kmormiles(): 
    selected = radio_state.get()
    if selected == 1: 
        fromtxt = "Miles"
        totxt = "Km"
    elif selected == 2: 
        fromtxt = "Km"
        totxt = "Miles"
    from_label.config(text=fromtxt)
    to_label.config(text=totxt)

def docalc():
    selected = radio_state.get()
    if selected == 1: 
        milestokm()
    elif selected == 2: 
        kmtomiles()

radio1 = Radiobutton(text="Miles to Km", value=1, variable=radio_state, command=kmormiles)
radio2 = Radiobutton(text="Km to Miles", value=2, variable=radio_state, command=kmormiles)
radio1.select()
radio1.grid(row=0, column=0)
radio2.grid(row=1, column=0)

input = Entry()
input.grid(row=1, column=1)

from_label = Label(text=fromtxt)
from_label.grid(row=1, column=2)

equal_label = Label(text="is equal to: ")
equal_label.grid(row=2, column=0)

to_label = Label(text = totxt)
to_label.grid(row=2, column=2)

outcome = Label(text = to)
outcome.grid(row=2, column=1)

calculate = Button(text = "Calculate", command = docalc )
calculate.grid(row=4, column=1)




window.mainloop()