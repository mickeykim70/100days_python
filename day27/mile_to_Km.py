import tkinter as tk

window = tk.Tk()
window.title('Mile to Km')
window.config(padx=20, pady=20)

#Converting function
def mile_converter():
    km = float(input_miles.get()) * 1.609
    kilometers = round(km, 2)
    numbers.config(text=km)


#Input miles (1st row in center)
input_miles = tk.Entry(window, width=7)
input_miles.grid(row=0, column=1)

#Label(Miles)
miles = tk.Label(window, text='Miles')
miles.grid(row=0, column=2)

#Label(is_equal_to)
is_equal_to = tk.Label(window, text='is equal to')
is_equal_to.grid(row=1, column=0)


#Label(numbers)
numbers = tk.Label(window, text= '0')
numbers.grid(row=1, column=1)


#Label(Km)
km = tk.Label(window, text= 'Km')
km.grid(row=1, column=2)

#Button(Calculate)
calc_button = tk.Button(window, text='Calculate',command=mile_converter)
calc_button.grid(row=2, column=1)









window.mainloop()