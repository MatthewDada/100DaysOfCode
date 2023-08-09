from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609, 1)
    km_input.config(text=f"{km}")

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=150)
window.config(padx=20, pady=20)

miles_input = Entry()
miles_input.grid(column=1, row=1)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=2)

km_input = Label(text="0")
km_input.grid(column=1, row=2)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=2)

button = Button(text="Calculate", width=10, height=2, command=miles_to_km)
button.grid(column=1, row=3)


window.mainloop()
