
# ---------------------------- CONSTANTS ------------------------------- #
from tabnanny import check
import tkinter
from turtle import st
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
#https://www.colorhunt.com

# ---------------------------- GLOBAL VARIABLES ------------------------------- #
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    """
    Reset timer.
    """
    global timer
    global reps

    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    """
    Start timer.
    """
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    reps += 1

    # 1st/3rd/5th/7th rep
    if reps % 8 == 0:
        print("Long break")
        title_label.config(text="Long break", fg=RED)
        count_down(long_break_sec)

    # 8th rep
    if reps % 2 == 0:
        print("Short break")
        title_label.config(text="Short break", fg=PINK)
        count_down(short_break_sec)

    # 2nd/4th/6th rep
    else:
        print("Work")
        title_label.config(text="Work", fg=GREEN)
        count_down(work_sec)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    """
    Recursive countdown function. Count from `count` to zero.
    """
    global timer
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:   
        timer = window.after(1, count_down, count-1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✔️"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

#
# main
#
if __name__ == "__main__":
    window = tkinter.Tk()
    window.title("Pomodoro")
    window.config(padx=100, pady=50, bg=YELLOW)

    title_label = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
    title_label.grid(column=1, row=0)

    tomato_img = tkinter.PhotoImage(file="tomato.png")

    canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
    canvas.create_image(100, 112, image=tomato_img)
    timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
    canvas.grid(column=1, row=1)

    start_button = tkinter.Button(text="Start", highlightthickness=0, command=start_timer)
    start_button.grid(column=0, row=2)

    reset_button = tkinter.Button(text="Reset", highlightthickness=0, command=reset_timer)
    reset_button.grid(column=2, row=2)

    check_marks = tkinter.Label(text="", fg=GREEN, bg=YELLOW, highlightthickness=0)
    check_marks.grid(column=1, row=3)

    window.mainloop()