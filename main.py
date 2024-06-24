from tkinter import *
from tkinter import messagebox
import random
import string
import json


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website_name = website_input.get()
    with open("data.json", "r") as file:
        data = json.load(file)
        if website_name in data:
            email = data[website_name]["email"]
            password = data[website_name]["password"]
            messagebox.showinfo(title=website_name, message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No Data Found for {website_name}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password_input.delete(0, END)

    letters = list(string.ascii_letters)
    numbers = list(string.digits)
    symbols = list(string.punctuation)
    password = [letters, numbers, symbols]

    finalPassword = ''
    password_num = random.randint(12, 18)

    for num in range(password_num):
        mix_pass = random.choice(password)
        finalPassword += random.choice(mix_pass)

    print(finalPassword)
    password_input.insert(END, finalPassword)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    data_s = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) != 0 and len(email) != 0 and len(password) != 0:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(data_s, file, indent=4)
        else:
            data.update(data_s)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)
    else:
        messagebox.showinfo(title='Oops', message="Please dont leave the field empty")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Logo Canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Website Label, Entry And Search Button
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

website_input = Entry(width=21)
website_input.focus()
website_input.grid(column=1, row=1)

search_button = Button(text='Search', command=find_password)
search_button.grid(column=2, row=1)

# Email/Username Label And Entry
email_label = Label(text='Email:')
email_label.grid(column=0, row=2)

email_input = Entry(width=35)
email_input.insert(END, 'example@gmail.com')
email_input.grid(column=1, row=2, columnspan=2)

# Password Label, Entry And Button
password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

password_button = Button(text='Generate Password', command=generate_password)
password_button.grid(column=2, row=3)

# Add Button
add_button = Button(text='Add', width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
