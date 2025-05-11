import json
from tkinter import *
import random
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generatePass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(symbols) for _ in range(random.randint(2, 4))]


    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if not website or not email or not password:
        messagebox.showerror(title="No Arguments", message="Enter some valid strings to input")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details that you have entered\nEmail: {email}\nPassword: {password}")
        if is_ok:
            with open("data.json","w") as file:
                json.dump(new_data, file, indent=4)
                website_entry.delete(0,END)
                password_entry.delete(0,END)
                messagebox.showinfo(title="success!", message="All things are saved in data file")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=20,pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = Entry(width=36)
website_entry.grid(column=1, row=1, columnspan=2)

email_label = Label(text="Email/Username:")
email_entry = Entry(width=36)
email_entry.grid(column=1, row=2, columnspan=2)
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)
password_label.grid(column=0, row=3)


#Buttons
gen_pass_btn = Button(text="Generate Password", command=generatePass)
gen_pass_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=36, command=save_pass)
add_btn.grid(column= 1, row=4 ,columnspan=2)


window.mainloop()
