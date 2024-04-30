import tkinter as tk
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Pomodor")
window.config(padx=100, pady=50, bg=YELLOW)

#Tomato
canvas = tk.Canvas(window, width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image = tomato_img)
canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

#Timer - Label
timer_label = tk.Label(window, text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timer_label.grid(column=1, row=0)


#Start - Button
start_button = tk.Button(window, text="Start", font="Verdana", highlightthickness=0)
start_button.grid(column=0, row=2)

#Reset - Button
reset_button = tk.Button(window, text="Reset", font="Verdana", highlightthickness=0)
reset_button.grid(column=2, row=2)

#checker - Label
checker_label = tk.Label(window, text="✔", fg=GREEN, bg=YELLOW)
checker_label.grid(column=1, row=3)

window.mainloop()
