from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- GENERATE WORD ------------------------------- #

data_df = pandas.read_csv("./src/data/french_words.csv")

to_learn = data_df.to_dict(orient="records")
print(to_learn)

#print(random.choice(all_words_df["French"]))
def next_card():
    current_card = random.choice(to_learn)
    print(current_card["French"])
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])  



















# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="./src/images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400,150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


#buttons
wrong_image = PhotoImage(file="./src/images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="./src/images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=next_card)
right_button.grid(column=1, row=1)


next_card()


window.mainloop()