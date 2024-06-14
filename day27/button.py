import tkinter as tk


window = tk.Tk()
window.title("Widget Examples")
window.minsize(500, 600)


def click_me():
    i = input_text.get()
    my_label.config(text=i)

#Label
my_label = tk.Label(text='Hello World')
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

#Button
my_button1 = tk.Button(text="Click Me", command=click_me)
my_button1.grid(column=2, row=0)

my_button2 = tk.Button(text="2nd button", command=click_me)
my_button2.grid(column=1, row=1)

#Entry
input_text = tk.Entry(width=10)
input_text.grid(column=3, row=2)


window.mainloop()



