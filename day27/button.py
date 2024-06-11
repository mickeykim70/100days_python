import tkinter as tk


window = tk.Tk()
window.title("Widget Examples")
window.minsize(500, 600)

#Label

my_label = tk.Label(text='Hello World', font=('Arial', 15))
my_label.pack()


def click_me():
    i = input_text.get()
    my_label.config(text=i)



#Button
my_button = tk.Button(text="Click Me", command=click_me)
my_button.pack()

#Entry
input_text = tk.Entry(width=10)

input_text.pack()



window.mainloop()



