import tkinter as tk

root = tk.Tk()
# root.geometry('400x250')
root.title('Miles to Km Converter')
root.config(padx=20, pady=20)


def display_km():
    miles = entry_miles.get()
    km = float(miles) * 1.609
    label_km.config(text=km)

#Entry (1, 0)
entry_miles = tk.Entry(root, width=5)
entry_miles.focus()
entry_miles.grid(column=1, row=0)


#Label (1, 1)
label_miles = tk.Label(root, text='Miles', font=('Helvetica', 15))
label_miles.grid(column=2, row=0)


label_isEqualTo = tk.Label(root, text='is equal to', font=('Helvetica', 15))
label_isEqualTo.grid(column=0, row=1)

label_km = tk.Label(root, text='0', font=('Helvetica', 15))
label_km.grid(column=1, row=1)

label_km2 = tk.Label(root, text='Km', font=('Helvetica', 15))
label_km2.grid(column=2, row=1)


button_calculator = tk.Button(root, text='Calculate', command=display_km , font=('Helvetica', 15))
button_calculator.grid(column=1, row=3)






root.mainloop()

