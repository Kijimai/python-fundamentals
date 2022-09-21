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

csv_data = pd.read_csv('./data/french_words.csv')
# List of dictionaries
to_learn_list = csv_data.to_dict(orient="records")
print(to_learn_list)

# ================================= INTERACTIVITY


def next_card():
    current_choice = choice(to_learn_list)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_choice["French"])


def x_out():
    print("X out")
    next_card()
    pass


def check_out():
    print("Check out")
    next_card()
    pass

# ================================= UI SETUP


# WINDOW RELATED
window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
card_front_img = PhotoImage(file=CARD_FRONT)
card_back_img = PhotoImage(file=CARD_BACK)

# CANVAS RELATED
canvas = Canvas(window, width=800, height=526,
                bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=card_front_img)
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
