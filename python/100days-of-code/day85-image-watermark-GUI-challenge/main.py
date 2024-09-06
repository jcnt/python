# assignment porgram for python GUI
# Day 85: write a GUI program to put watermark on images
#
import os
import shutil
import tkinter as tk
from tkinter import filedialog

from PIL import Image, ImageDraw, ImageFont


def browse_files():
    os.remove("temp.png")
    filename = filedialog.askopenfilename(
        initialdir="~/",
        title="Select a file",
        filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png")),
    )
    image_path.config(text=filename)
    jpg = Image.open(filename)
    small = (300, 300)
    jpg.thumbnail(small)
    jpg.save("temp.png")
    global prepng
    prepng = tk.PhotoImage(file="temp.png")
    canvas.itemconfig(canvimg, image=prepng)


def watermark_image():
    os.remove("watermarked_image.png")
    orig_image = Image.open(image_path.cget("text"))
    draw = ImageDraw.Draw(orig_image)
    wm_text = image_watermark.get()
    if wm_text == "":
        tk.messagebox.showwarning(title="Warning", message="Watermark was not provided")

    font_size = 20
    font = ImageFont.truetype("Arial", font_size)
    text_color = (255, 255, 255)
    text_height = font_size
    text_width = draw.textlength(wm_text, font)
    image_width, image_height = orig_image.size
    margin = 10
    position = (image_width - text_width - margin, image_height - text_height - margin)
    #    draw.text(position, wm_text, font=font, fill=text_color)
    draw.text(position, wm_text, font=font)
    orig_image.save("watermarked_image.png")
    orig_image.show()


window = tk.Tk()
window.title("Image Watermark")
window.minsize(width=400, height=500)
window.config(padx=50, pady=50)

main_label = tk.Label(text="Please upload an image.")
main_label.grid(row=0, column=1)

image_label = tk.Label(text="Please select the image.")
image_label.grid(row=2, column=0)

image_path = tk.Label(text="")
image_path.grid(row=2, column=1)

browse = tk.Button()
browse.grid(row=2, column=2)
browse.config(text="Browse", command=browse_files)

input_label = tk.Label(text="Enter the text: ")
input_label.grid(row=3, column=0)
image_watermark = tk.StringVar()
input_entry = tk.Entry(textvariable=image_watermark)
input_entry.grid(row=3, column=1)

watermark = tk.Button()
watermark.grid(row=4, column=1)
watermark.config(text="Watermark", command=watermark_image)

canvas = tk.Canvas(width=300, height=300)
shutil.copyfile("black.png", "temp.png")
prepng = tk.PhotoImage(file="temp.png")
blackimg = tk.PhotoImage(file="black.png")
canvimg = canvas.create_image(150, 150, image=blackimg)
canvas.grid(row=5, column=0, rowspan=3, columnspan=3)

window.mainloop()
