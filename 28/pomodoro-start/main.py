from tkinter import *
from playsound import playsound
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.01
SHORT_BREAK_MIN = 0.01
LONG_BREAK_MIN = 20
APP_NAME = "Pomodoro Timer"
reps = 0
timer = None


def play_timer_sound():
    playsound('completed-ding-3.wav')

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    check_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    app_label.config(text=APP_NAME)

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        app_label.config(text="Long Break Time!", font=(
            FONT_NAME, 20, "bold"), bg=YELLOW, fg=RED)
        play_timer_sound()            
        countdown(long_break_sec)
    elif reps % 2 == 0:
        app_label.config(text="Break Time!", font=(
            FONT_NAME, 20, "bold"), bg=YELLOW, fg=PINK)
        play_timer_sound()
        countdown(short_break_sec)
    else:
        app_label.config(text="Work!", font=(
            FONT_NAME, 20, "bold"), bg=YELLOW, fg=GREEN)
        countdown(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    count_min = math.floor(count/60)
    count_seconds = count % 60
    if count_seconds <= 9:
        count_seconds = f"0{count_seconds}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps / 2)):
            marks += check
        check_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #


fg = GREEN
check = "✔"
window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)


bg = PhotoImage(file='./tomato.png')

app_label = Label(text=APP_NAME, font=(
    FONT_NAME, 20, "bold"), bg=YELLOW, fg=RED)
app_label.grid(column=1, row=0)

canvas = Canvas(window, width=202, height=226, bg=YELLOW, highlightthickness=0)
canvas.create_image(102, 112, image=bg)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


check_label = Label(fg=GREEN, bg=YELLOW, font=36)
check_label.grid(row=3, column=1)

# ****** Start and Reset Buttons ********
start_btn = Button(text="Start", command=start_timer)
reset_btn = Button(text="Reset", command=reset_timer)
start_btn.grid(column=0, row=2)
reset_btn.grid(column=2, row=2)

window.mainloop()
