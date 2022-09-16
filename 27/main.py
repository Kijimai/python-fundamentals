from tkinter import *

window = Tk()
window.title("Skyrim: Collector's Edition")
window.minsize(width=500, height=700)

# Label
my_label = Label(text="I am a label", font=("Arial", 20, "bold"))
my_label.pack(side="top")
# my_label["text"] = "renamed label"
# my_label.config(text="renamed through the config")


input = Entry(width=10)
input.insert(END, "email")
input.pack()
input.focus()

# height - number of row size, width - number of col size
textbox = Text(bg="white", height=5, width=30)
textbox.pack()
# END -- an index to allow Tkinter to figure out which item you are referring to
textbox.insert(END, "Some text here...")
# .get() requires two arguments a start and an end position, the 1.0 represents line1, char 0
# END is the ending point of the whole text line
print(textbox.get("1.0", END))

def get_scale_val(val):
    print(val)


my_scale = Scale(command=get_scale_val)
my_scale.pack()


def get_spin_value():
    print(my_spinbox.get())


my_spinbox = Spinbox(from_=0, to=10, width=5, command=get_spin_value)
my_spinbox.pack()


def button_click():
    if input.get() == "":
        return
    my_label["text"] = input.get()


button = Button(text="Click Me", command=button_click)
button.pack(side="top")


def checkbutton_used():
    print(checked_state.get())


# returns 1 or 0 if on or off - IntVar is Tkinter class
checked_state = IntVar()
check_button = Checkbutton(
    text="Remember Me", variable=checked_state, command=checkbutton_used)
check_button.pack()

# Radio buttons

def radio_used():
    print(radio_state.get())

# variable to hold on top which radio button value is checked
# When a radio button is clicked, the value of the checked button is stored in "radio_state". Both buttons have a function attached to them that will print the current value of the radio_state button
radio_state = IntVar()
radio1 = Radiobutton(text="Option 1", value=1, variable=radio_state, command=radio_used)
radio2 = Radiobutton(text="Option 2", value=2, variable=radio_state, command=radio_used)
radio1.pack()
radio2.pack()




# Listbox
def listbox_used(e):
  print(f"Event: {e}")
  print(my_listbox.get(my_listbox.curselection()))

my_listbox = Listbox(height=4)
fruits = ["apple", "oranges", "pear", "bnanan"]
for fruit in fruits:
  my_listbox.insert(fruits.index(fruit), fruit)
my_listbox.bind("<<ListboxSelect>>", listbox_used)
my_listbox.pack()


window.mainloop()
