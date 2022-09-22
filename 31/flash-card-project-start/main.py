import pandas as pd
from tkinter import *
from random import choice, randint
# ================================= CONSTANTS
WRONG_IMG = './images/wrong.png'
RIGHT_IMG = './images/right.png'
CARD_FRONT = './images/card_front.png'
CARD_BACK = './images/card_back.png'

LANGUAGE_FONT_SETTINGS = ("Ariel", 40, "italic")
DEFINITION_FONT_SETTINGS = ("Ariel", 60, "bold")

BACKGROUND_COLOR = "#B1DDC6"

# Flip delay in milliseconds
FLIP_DELAY = 3000
try:
    csv_data = pd.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pd.read_csv('./data/french_words.csv')
    to_learn_list = original_data.to_dict(orient="records")
else:
    to_learn_list = csv_data.to_dict(orient="records")
# List of dictionaries
list_cleared = False
current_choice = {}
learned_words = []
# ================================= INTERACTIVITY


def close_app():
    window.destroy()


def next_card():
    global list_cleared
    if list_cleared:
        return
    global current_choice, flip_timer
    # cancel the current timer running -- reassigns it after this function goes through all of its actions
    window.after_cancel(flip_timer)
    if len(to_learn_list) > 0:
        current_choice = choice(to_learn_list)
        canvas.itemconfig(card_title, text="French", fill="black")
        canvas.itemconfig(
            card_word, text=current_choice["French"], fill="black")
        canvas.itemconfig(card_bg, image=card_front_img)
        flip_timer = window.after(FLIP_DELAY, to_english)
    else:
        list_cleared = True
        canvas.itemconfig(card_title, text="Congratulations!", fill="black")
        canvas.itemconfig(
            card_word, text="You've learned all the words in the list!", font=("Ariel", 30, "bold"))
        wrong_btn.configure(image=None,
                            text="Exit", highlightthickness=0, command=close_app)
        right_btn.configure(image=None,
                            text="Restart", highlightthickness=0, command=check_out)


def to_english():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_choice["English"], fill="white")
    canvas.itemconfig(card_bg, image=card_back_img)


def x_out():
    next_card()


def check_out():
    learned_words.append(current_choice)
    is_known()
    save_progress()


def save_progress():
    words_to_learn_saved = pd.DataFrame(to_learn_list)
    words_to_learn_saved.to_csv('./data/words_to_learn.csv', index=False)


def is_known():
    global current_choice
    try:
        to_learn_list.remove(current_choice)
    except ValueError:
        return    
    else:
        next_card()

# ================================= UI SETUP


# WINDOW RELATED
window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(FLIP_DELAY, to_english)


card_front_img = PhotoImage(file=CARD_FRONT)
card_back_img = PhotoImage(file=CARD_BACK)

# CANVAS RELATED
canvas = Canvas(window, width=800, height=526,
                bg=BACKGROUND_COLOR, highlightthickness=0)
card_bg = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(
    400, 150, font=LANGUAGE_FONT_SETTINGS)
card_word = canvas.create_text(
    400, 263, font=DEFINITION_FONT_SETTINGS)
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
wrong_img = PhotoImage(file=WRONG_IMG)
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=x_out)
wrong_btn.grid(column=0, row=1)

right_img = PhotoImage(file=RIGHT_IMG)
right_btn = Button(image=right_img, highlightthickness=0, command=check_out)
right_btn.grid(column=1, row=1)

next_card()
window.mainloop()
