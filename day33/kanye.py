import tkinter as tk
import requests


FONT = ("Arial", 20, "bold")


def display_quote():

    # API setting
    response = requests.get(url="https://api.kanye.rest/")
    response.raise_for_status()

    data = response.json()
    canvas.itemconfig(kanye_says, text=data["quote"])


# -------------------- UI --------------- #
root = tk.Tk()
root.title("Kanye says...")
root.config(padx=50, pady=50)

background_img = tk.PhotoImage(file="background.png")

canvas = tk.Canvas(root, width=300, height=414)
canvas.create_image(150, 207, image=background_img)
kanye_says = canvas.create_text(150, 207, text="Kanye says...", font=FONT, fill='white')
canvas.grid(column=0, row=0)

kanye_img = tk.PhotoImage(file="kanye.png")

kanye_btn = tk.Button(root, image=kanye_img, highlightthickness=0, command=display_quote)
kanye_btn.grid(column=0, row=1)


root.mainloop()
