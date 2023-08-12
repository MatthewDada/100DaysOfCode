from tkinter import *
import pandas as pd
from random import randint, choice

BACKGROUND_COLOR = "#B1DDC6"
random_choice = {}

try:
    data = pd.read_csv("day 31-40\\flash card\\data\\words_to_learn.csv")
except FileNotFoundError or OSError:
    original_data = pd.read_csv("day 31-40\\flash card\\data\\french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global random_choice, flip_timer
    window.after_cancel(flip_timer)
    random_choice = choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=random_choice["French"], fill="black")
    canvas.itemconfig(card_bg, image=front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=random_choice["English"])
    canvas.itemconfig(card_bg, image=back_img)


def is_known():
    global random_choice
    to_learn.remove(random_choice)
    print(len(to_learn))
    data_left = pd.DataFrame(to_learn)
    data_left.to_csv("day 31-40\\flash card\\data\\words_to_learn.csv", index=False)

    next_card()


window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0)
front_img = PhotoImage(file="day 31-40\\flash card\\images\\card_front.png")
back_img = PhotoImage(file="day 31-40\\flash card\\images\\card_back.png")
card_bg = canvas.create_image(400, 263, image=front_img)
canvas.config(background=BACKGROUND_COLOR)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 40, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

check_image = PhotoImage(file="day 31-40/flash card/images/right.png")
check_button = Button(image=check_image, highlightthickness=0, command=is_known)
check_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="day 31-40/flash card/images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

next_card()

window.mainloop()
