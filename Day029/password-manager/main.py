from audioop import add
from calendar import c
from msilib.schema import CompLocator
from tkinter import *
from turtle import title, width
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """
    Generates a random password.
    """
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(0, nr_letters)]
    password_symbols = [choice(symbols) for _ in range(0, nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(0, nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    if len(password_entry.get()) != 0:
        password_entry.delete(0, END)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """
    Saves website/email/password combination to txt file.
    """
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Ooops...", message="Please make sure to enter a valid website/password")
    else:
        is_ok_to_save = messagebox.askokcancel(title=website, message=f"These are the defails entered:\n\n Email: {email}\n Password: {password}\n\n Is it ok to save?")

        if is_ok_to_save:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                
# ---------------------------- UI SETUP ------------------------------- #

if __name__ == "__main__":
    
    window = Tk()
    window.title("Password Manager")
    window.config(padx=40, pady=40)

    logo_img = PhotoImage(file="logo.png")

    canvas = Canvas(width=200, height=200, highlightthickness=0)
    canvas.create_image(100, 100, image=logo_img)
    canvas.grid(column=1 ,row=0)

    # Labels
    website_label = Label(text="Website:")
    website_label.grid(column=0, row=1)
    email_label = Label(text="Email/Username:")
    email_label.grid(column=0, row=2)
    password_label = Label(text="Password:")
    password_label.grid(column=0, row=3)

    # Entries
    email_entry = Entry(width=35)
    email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
    email_entry.insert(0, "michotitonegrogordoycabezon@hohotnail.com")
    website_entry = Entry(width=35)
    website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
    website_entry.focus()
    password_entry = Entry(width=32, show="*")
    password_entry.grid(column=1, row=3, sticky="W")

    # Buttons
    password_button= Button(text="Generate Password", command=generate_password)
    password_button.grid(column=2, row=3, sticky="EW")
    add_button= Button(text="Add", width=36, command=save)
    add_button.grid(column=1, row=4, columnspan=2, sticky="EW")


    window.mainloop()