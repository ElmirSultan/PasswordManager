from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

import random

def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [random.choice(letters) for _ in range(randint(0,10))]
    password_symbols = [random.choice(symbols) for _ in range(randint(2,4))]
    password_numbers = [random.choice(numbers) for _ in range(randint(2,4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password_generated = "".join(password_list)
    password_entry.insert(0,password_generated)
    
    pyperclip.copy(password_generated)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.askokcancel(title="Oops",message=f"You left forms empty, plesae fill all of them")
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"These are the detail are entered: \nEmail: {email}\nPassword:{password} \nis it OK to save?")
        if is_ok:
            with open("mydoc.txt","a") as my_document:
                my_document.write(f"{website} | {email} | {password} \n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)
    
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=20)
  
canvas = Canvas(height=200,width=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_image)
canvas.grid(row=0,column=1)


website_label = Label(text="Website:")
website_label.grid(row=1,column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2,column=0)

password_label = Label(text="Password:")
password_label.grid(row=3,column=0)

website_entry = Entry(width=48)
website_entry.grid(row=1,column=1,columnspan=2)

email_entry = Entry(width=48)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"elmirsultann@gmail.com")

password_entry = Entry(width=30)
password_entry.grid(row=3,column=1)

# Buttons

generate_password_button = Button(text="Generate Password",command=generate_password)
generate_password_button.grid(row=3,column=2)

add_button = Button(text="Add",width=43,command=save)
add_button.grid(row=4,column=1,columnspan=2)


window.mainloop()