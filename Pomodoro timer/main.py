import math
from os import times_result
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer, reps
    window.after_cancel(timer)
    title_label.config(text="Timer", fg=GREEN)
    checkMark.config(text="")
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Short Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(num):
    global mark
    count_min = math.floor(num / 60)
    count_seconds = num % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"



    canvas.itemconfig(timer_text, text=f"{count_min}:{count_seconds}")
    if num > 0:
        global timer
        timer = window.after(1000, count_down, num - 1)
    else:
        start_timer()
        work_sessions = math.floor(reps/2)
        mark = ""
        for _ in range(work_sessions):
            mark += "✅"
        checkMark.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW, highlightthickness=0)

canvas = Canvas(width=200, height=224,bg=YELLOW)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(102,112,image = tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1,row=1)

title_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50, "bold"), bg=YELLOW)
title_label.grid(column=1,row=0)


start_btn = Button(text="Start",highlightthickness=0, command=start_timer)
start_btn.grid(column=0,row=2)
reset_btn = Button(text="Reset",highlightthickness=0, command=reset_timer)
reset_btn.grid(column=2,row=2)

checkMark = Label(text="", fg=GREEN)
checkMark.grid(column=1,row=3)


window.mainloop()