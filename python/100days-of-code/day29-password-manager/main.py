from tkinter import * 
from tkinter import messagebox
from random import shuffle, randint, choice
# import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

randpassword = ""

def pwgen():
    global randpassword
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    randletters = [ choice(letters) for _ in range(randint(8, 10)) ]
    randnumbers = [ choice(numbers) for _ in range(randint(2, 4)) ]
    randsymbols = [ choice(symbols) for _ in range(randint(2, 4)) ]
    
    randomlist = randletters + randnumbers + randsymbols
    shuffle(randomlist)
    randpassword = "".join(randomlist)
    passwinput.delete(0, END)
    passwinput.insert(0, randpassword)
#    pyperclip.copy(randpassword)

# ---------------------------- SAVE PASSWORD ------------------------------- #
#    messagebox.showinfo(title="test", message="message")

def savepw(): 
    website = webinput.get()
    user = userinput.get()
    passwd = passwinput.get()
    json_data = {
        website: {
            "email": user, 
            "password": passwd, 
        }
    }

    if len(website) == 0 or len(passwd) == 0: 
        messagebox.showwarning(title="Empty field", message="Please don't let the fields empty!")
    else:
        try: 
            with open("password.json", "r") as file: 
                data = json.load(file)
        except:
            with open("password.json", "w") as file:
                json.dump(json_data, file, indent=4)
        else: 
            data.update(json_data)

            with open("password.json", "w") as file:
                json.dump(data, file, indent=4)
        finally: 
            webinput.delete(0, END)
            passwinput.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    try: 
        with open("password.json", "r") as file: 
            data = json.load(file)
    except: 
        messagebox.showwarning(title="Warning", message="No password file!")

    
    website = webinput.get()
    if website in data: 
        email = data[website]["email"]
        password = data[website]["password"]
        messagebox.showinfo(title=website, message=f"e-mail: {email}\npassword: {password}")
    else:
        messagebox.showwarning(title="Warning", message="Website not found!")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
passwdimage = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=passwdimage) # 100, 100 is the position on canvas
canvas.grid(row=0, column=1)

website = Label(text="Website:", bg="white", fg="black")
website.grid(row=1, column=0)

email = Label(text="E-mail/Username:", bg="white", fg="black")
email.grid(row=2, column=0)

passlabel = Label(text="Password:", bg="white", fg="black")
passlabel.grid(row=3, column=0)

webinput = Entry(width=21, highlightthickness=0)
webinput.focus()
webinput.grid(row=1, column=1)

userinput = Entry(width=39, highlightthickness=0)
userinput.insert(0, "yyaazz@gmail.com")
userinput.grid(row=2, column=1, columnspan=2)

passwinput = Entry(width=21, highlightthickness=0)
passwinput.grid(row=3, column=1)

search = Button(text="Search", width=14, highlightthickness=0, command=find_password)
search.grid(row=1, column=2)

generate = Button(text="Generate Password", width=14, highlightthickness=0, command=pwgen)
generate.grid(row=3, column=2)

add = Button(text="Add", width=36, highlightthickness=0, command=savepw)
add.grid(row=4, column=1, columnspan=2)


# -------------------- mandatory --------------------
window.mainloop()

