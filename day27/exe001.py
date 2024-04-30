from tkinter import *


def button_clicked():
    new_text = input_text.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.geometry("500x300")
window.config(padx=100, pady=200)

#Label

my_label = Label(window, text="My Label", font=("Arial", 24, "bold"))
# my_label.pack(side=LEFT)
my_label.grid(column=0, row=0)

my_button1 = Button(text="Click Me", command=button_clicked)
my_button1.grid(column=1, row=1)

my_button2 = Button(text="Button 2", command=button_clicked)
my_button2.grid(column=2, row=0)

input_text = Entry(window)
input_text.grid(column=3, row=2)

window.mainloop()

