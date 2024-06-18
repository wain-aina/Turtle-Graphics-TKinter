from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
random_word = {}
data = {}

try:
    original = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    data = original_data.to_dict(orient="records")
else:
    data = original.to_dict(orient='records')


def new_word():
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    random_word = data[random.randint(0, len(data))]
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word, text=random_word["French"], fill="black")
    canvas.itemconfig(card_background, image=front)
    flip_timer = window.after(3000, func=translation)

def translation():
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=random_word['English'], fill="white")
    canvas.itemconfig(card_background, image=back)

def is_not_known():
    data.remove(random_word)
    to_learn = pd.DataFrame(data)
    to_learn.to_csv("data/words_to_learn.csv", index=False)
    new_word()


window = Tk()
window.title("Flash Cards")
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=translation)

canvas = Canvas(width=800, height=526, highlightthickness=0)

back = PhotoImage(file="images/card_back.png")
front = PhotoImage(file="images/card_front.png")
right = PhotoImage(file='images/right.png')
wrong = PhotoImage(file='images/wrong.png')

card_background = canvas.create_image(400, 263, image=front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
language = canvas.create_text(400, 150, text="title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="word", font=("Ariel", 40, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

#Buttons
green = Button(image=right, highlightthickness=0, command=new_word)
green.grid(row=1, column=0)

red = Button(image=wrong, highlightthickness=0, command=is_not_known)
red.grid(row=1, column=1)

window.mainloop()


