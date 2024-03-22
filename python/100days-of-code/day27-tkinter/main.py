from tkinter import * 

window = Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)
window.config(padx=10, pady=10)

# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
# my_label.pack(side="left")
my_label.grid(row=0, column=0)

# Entry 
input = Entry()
# input.pack()
input.grid(row=3, column=4)

# button

def button_click():
#     my_label.config(text="Button got clicked")
    textbox = input.get()
    my_label.config(text=textbox)
    
button = Button(text = "Click me", command= button_click)
# button.pack()
button.grid(row=1, column=1)

button_new = Button(text= "new button")
button_new.grid(row=0, column=2)

window.mainloop()