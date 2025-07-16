from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 24
SHORT_BREAK_MIN = 4
LONG_BREAK_MIN = 19
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        title_label.config(text="Break", font=(FONT_NAME, 40, "bold"), fg=RED, bg=YELLOW)
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        title_label.config(text="Break", font=(FONT_NAME, 40, "bold"), fg=PINK, bg=YELLOW)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        title_label.config(text="Work", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
        count_down(WORK_MIN * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = round(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer =  window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range (int(reps/2)):
            marks += "✔"
        check_marks.config(text=marks)




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=100, pady=50, bg=YELLOW)
window.title("Pomodoro Timer")

title_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

photo = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 110, image=photo)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()