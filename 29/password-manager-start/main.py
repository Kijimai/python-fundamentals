from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_pass():
    pass_entry.delete(0, END)
    generated = []

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    generated += [choice(letters) for _ in range(nr_letters)]
    generated += [choice(numbers) for _ in range(nr_numbers)]
    generated += [choice(symbols) for _ in range(nr_symbols)]

    shuffle(generated)
    new_pass = ''.join(generated)
    pyperclip.copy(new_pass)
    pass_entry.insert(0, new_pass)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    web_name = website_entry.get()
    email_user_name = email_user_entry.get()
    password = pass_entry.get()
    if not web_name or not email_user_name or not password:
        messagebox.showwarning(message="Please dont leave a field empty!")
        confirmation_label.config(text="Don't leave a field empty!", fg='red')
        return
    answer = messagebox.askquestion(
        title="Save Data?", message=f"Are you sure you want to save this info?\nWebsite name: {web_name}\nEmail/Username: {email_user_name}\nPassword: {password}")
    if answer == "no":
        return
    with open('./data.txt', mode="a") as data:
        data.writelines(f"{web_name} | {email_user_name} |{password}\n")
    website_entry.delete(0, END)
    email_user_entry.delete(0, END)
    pass_entry.delete(0, END)
    confirmation_label.config(text="Entries saved to data.txt!", fg='green')
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

lock_image = PhotoImage(file="./logo.png")

# Canvas
canvas = Canvas(window, width=200, height=200)
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
email_user_label = Label(text="Email/Username:")
pass_label = Label(text="Password:")
website_label.grid(column=0, row=1)
email_user_label.grid(row=2, column=0)
pass_label.grid(row=3, column=0)
confirmation_label = Label(font=("Arial", 16, "bold"), fg="green")
confirmation_label.grid(column=1, row=5)

# Buttons
generate_btn = Button(text="Generate Password", command=generate_pass)
add_btn = Button(text="Add", command=save_data)
generate_btn.grid(column=2, row=3)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")

# Entry inputs
website_entry = Entry()
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()
email_user_entry = Entry()
email_user_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_user_entry.insert(0, "dummyemail@yahoo.com")
pass_entry = Entry()
pass_entry.grid(column=1, row=3, sticky="EW")


window.mainloop()
