import tkinter as tk
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pw_letters = [choice(letters) for _ in range(randint(4, 6))]
    pw_numbers = [choice(numbers) for _ in range(randint(1, 4))]
    pw_symbols = [choice(symbols) for _ in range(randint(1, 2))]

    pw_list = pw_letters + pw_numbers + pw_symbols
    shuffle(pw_list)

    password = "".join(pw_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    #Verify the empty string
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo("Error", "Please enter all fields")
    else:
        try:
            with open('data.json', 'r') as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            #Updating old data with new data
            data.update(new_data)

            with open('data.json', 'w') as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, tk.END)
            website_entry.focus()
            email_entry.delete(0, tk.END)
            email_entry.insert(0, "abc@gmail.com")
            password_entry.delete(0, tk.END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo("Error", "No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"{email= }\n{password= }")
        else:
            messagebox.showinfo("Error", f"No {website} Data Found")
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
website_entry = tk.Entry(width=22)
website_entry.grid(column=1, row=1)
website_entry.focus()
email_entry = tk.Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "abc@gmail.com")
password_entry = tk.Entry(width=22)
password_entry.grid(column=1, row=3)


#Buttons
generate_password_button = tk.Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)
add_button = tk.Button(text="Add", width=34, command=save)
add_button.grid(column=1, row=4, columnspan=2)
search_button = tk.Button(text="Search", width=13, command=find_password)
search_button.grid(column=2, row=1)


window.mainloop()
