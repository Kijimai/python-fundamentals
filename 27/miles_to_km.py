from tkinter import *

window = Tk()
window.config(width=500, height=300, padx=20, pady=20)
window.title("Miles to Km Converter")

miles_entry = Entry(text="Miles", width=10)
miles_entry.grid(column=1, row=0)

label = Label(text="is equal to")
label.grid(column=0, row=1)

value_label = Label()
value_label["text"] = "0"
value_label.grid(row=1, column=1)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

km_label = Label(text="km")
km_label.grid(column=3, row=1)


def miles_to_km():
    value_label["text"] = str(round(float(miles_entry.get()) * 1.6, 1))


calculate_btn = Button(text="Calculate", command=miles_to_km)
calculate_btn.grid(column=1, row=2)
window.mainloop()
