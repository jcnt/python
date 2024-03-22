from tkinter import * 

window = Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)

# ----------------------------------------- Text 
text = Text(height=5, width=30)
text.focus()
text.insert(END, "Exemple multi line entry")
print(text.get("1.0", END))
text.pack()

# ----------------------------------------- Spinbox

def spinbox_used():
    print(spinbox.get())

spinbox = Spinbox(from_ = 0, to = 10, width = 5, command = spinbox_used)
spinbox.pack()

# ----------------------------------------- Check button
def checkbutton_used():
    print(checked_state.get())

checked_state = IntVar()
checkbutton = Checkbutton(text = "is on?", variable=checked_state, command = checkbutton_used)
checked_state.get()
checkbutton.pack()

# ----------------------------------------- Radio button
def radio_used():
    print(radio_state.get())

radio_state = IntVar()
radiobutton1 = Radiobutton(text = "Option1", value = 1, variable = radio_state, command = radio_used)
radiobutton2 = Radiobutton(text = "Option2", value = 2, variable = radio_state, command = radio_used)
radiobutton1.pack()
radiobutton2.pack()

# ----------------------------------------- Listbox
def listbox_used():
    print(listbox.get(listbox.curselection()))
listbox = Listbox(height=4)
fruits = ["Apple", "Banana", "Pear", "Orange"]
for i in fruits: 
    listbox.insert(fruits.index(i), i)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


window.mainloop()
