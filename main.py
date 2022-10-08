from tkinter import *
from tkinter import Label


def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    label4.config(text=f"{km}")
window = Tk()
window.title("Mile to Kilometer converter")
window.config(padx=20,pady=20)

#creatintg entry
miles_input = Entry(width=7)
miles_input.grid(row=0,column=1)

#creating labels
label1 = Label(text="is equal to")
label1.grid(row=1,column=0)

label2 = Label(text="Miles")
label2.grid(row=0,column=2)

label3 = Label(text="Km")
label3.grid(row=1,column=2)

label4 = Label(text="0")
label4.grid(row=1,column=1)

#creating buttom
miles_input_button = Button(text = "calculate",command = miles_to_km)
miles_input_button.grid(row=2,column=1)

window.mainloop()