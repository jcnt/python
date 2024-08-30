# assignment porgram for python GUI
# Day 85: write a GUI program to put watermark on images
#
from tkinter import Button, Entry, Label, Tk, filedialog


def browse_files():
    filename = filedialog.askopenfilename(initialdir="~/", title="Select a file")


window = Tk()
window.title("Image Watermark")
window.minsize(width=700, height=400)
window.config(padx=50, pady=50)

main_label = Label(text="Please upload an image.")
main_label.grid(row=0, column=1)

input_label = Label(text="Enter the text to watermark: ")
input_label.grid(row=2, column=0)
input = Entry()
input.grid(row=2, column=1)

browse = Button()
browse.grid(row=4, column=1)
browse.config(text="Browse", command=browse_files)

window.mainloop()


# Todo
# add filetypes to the browse window.
