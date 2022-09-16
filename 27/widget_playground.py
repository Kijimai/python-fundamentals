from tkinter import *

FONT = ("Arial", 24, "bold")


def button_clicked():
    print("Button Pressed!")


window = Tk()
window.title("My TKinter playground")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)
# Changing the side to left changes all of the elements to be left aligned - in the order they are made
# Instead, use "place". It uses x,y values
my_label = Label(text="Playground Label", font=FONT)

# Point begins at the top left, the x,y determines how far it is from that point, negatives go backwards
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)

my_button = Button(text="Click me", command=button_clicked)
my_button.config(padx=5, pady=10)
my_button.grid(column=1, row=1)
input = Entry(width=10)
input.grid(column=3, row=3)

new_button = Button(text="New Button!", command=button_clicked)
new_button.grid(column=2, row=0)

window.mainloop()
