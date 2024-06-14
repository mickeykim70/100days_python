import tkinter as tk

img = "logo.png"

# ----------------------------  PASSWORD GENERATOR ------------------------ #


# ----------------------------  SAVE PASSWORD ------------------------ #


# ----------------------------  UI SETUP ------------------------ #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=35, pady=35)

img_lock = tk.PhotoImage(file=img)

canvas = tk.Canvas(window, height=200, width=200)
canvas.create_image(100, 100, image=img_lock, anchor=tk.CENTER)
canvas.grid(column=1, row=0)

website_label = (tk.Label(window, text="Website"))
website_label.grid(column=0, row=1)
website_entry = tk.Entry(window, width=34)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_label = (tk.Label(window, text="Email/UserName:"))
email_label.grid(column=0, row=2)
email_entry = tk.Entry(window, width=34)
email_entry.insert(0, "mickeykim70@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)
password_label = tk.Label(window, text="Password:")
password_label.grid(column=0, row=3)
password_entry = tk.Entry(window, width=28)
password_entry.grid(column=1, row=3)
generate_button = tk.Button(window, text="G")
generate_button.grid(column=2, row=3)
add_button = tk.Button(window, text="Add", width=30)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
