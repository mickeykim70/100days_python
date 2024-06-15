import tkinter as tk
from tkinter import messagebox
import random
# import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
               'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
               'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
               'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pw_letters = [random.choice(letters) for _ in range(random.randint(4, 6))]
    pw_numbers = [random.choice(numbers) for _ in range(random.randint(1, 4))]
    pw_symbols = [random.choice(symbols) for _ in range(random.randint(1, 2))]

    pw_list = pw_letters + pw_numbers + pw_symbols
    random.shuffle(pw_list)

    password = "".join(pw_list)
    password_entry.insert(0, password)
    # pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_text = website_entry.get()
    email_text = email_entry.get()
    password_text = password_entry.get()

    saved_text = f"{website_text} | {email_text} | {password_text}\n"

    if website_text == "" or email_text == "" or password_text == "":
        messagebox.showinfo("Error", "Please enter all fields")
    else:
        is_ok = messagebox.askokcancel("Saving...", saved_text)
        if is_ok:

            with open("data.txt", "a") as file:
                file.write(saved_text)
                website_entry.delete(0, tk.END)
                email_entry.delete(0, tk.END)
                email_entry.insert(0, "abc@gmail.com")
                password_entry.delete(0, tk.END)


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
window.resizable(True, True)

#Canvas
canvas = tk.Canvas(window, width=200, height=200)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#Labels
website_label = tk.Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = tk.Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = tk.Label(text="Password:")
password_label.grid(column=0, row=3)


#Entries
website_entry = tk.Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_entry = tk.Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "abc@gmail.com")
password_entry = tk.Entry(width=30)
password_entry.grid(column=1, row=3)


#Buttons
generate_password_button = tk.Button(text="Gen", command=generate_password)
generate_password_button.grid(column=2, row=3)
add_button = tk.Button(text="Add", width=34, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()