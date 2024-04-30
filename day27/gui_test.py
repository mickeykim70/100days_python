from tkinter import *

window = Tk()
window.title("Widget Examples")
# window.minsize(500, 500)
window.geometry("500x500")

#Labels
label = Label(window, text="This is old text")
label.config(text="This new text", font=("Arial", 14))
label.pack()

#Buttons
def action():
    print("Do something")

#Calls action() when pressed
button = Button(window, text="Click Me", command=action)
button.pack()

#Entries
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, "Some text to begin with.")
entry_text = entry.get()
print(entry_text)
entry.pack()

#Text
text = Text(window, height=5, width=30)
#Put cursor in textbox
text.focus()
#Add some text to begin with
text.insert(END, "Example of multi-line text entry.")
print(text.get("1.0", END))
text.pack()

#Spinbox
def spinbox_used():
    print(spinbox.get())
spinbox = Spinbox(window, from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value
def scale_used(value):
    print(value)

scale = Scale(from_=0, to=100, orient=HORIZONTAL, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    print(checked_state.get())

checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())

radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=1, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ['Apple', 'Pear', 'Orange', 'Banana', 'Strawberry',]
for fruit in fruits:
    listbox.insert(END, fruit.index(fruit), fruit)
    listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


window.mainloop()

