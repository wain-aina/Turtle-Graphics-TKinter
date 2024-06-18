# from tkinter import *
#
# window = Tk()
#
# window.title("Miles2km")
# window.minsize(width=500, height=300)
# window.config(padx=20, pady=20)
#
# def btn_click():
#     user = input.get()
#     my_label.config(text=user)
#
# #Label
#
# my_label = Label(text="I'm a label", font=("arial", 24, "bold"))
# my_label.config(text="New Text")
# # my_label.pack()
# my_label.grid(column=0, row=0)
# my_label.config(padx=20, pady=20)
#
# #Entry
#
# input = Entry(width=10)
# # input.place(x=100, y=200)
# input.grid(column=3, row=2)
#
# #Button
#
# button = Button(text = "click me", command=btn_click)
# button.grid(column=1, row=1)
#
# #2nd Button
# new_btn = Button(text="I'm new here")
# new_btn.grid(column=2, row=0)
#
# window.mainloop()

from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(height=150, width=300)
window.config(pady=10, padx=10)

def convert():
    miles = float(input.get())
    km = round(miles * 1.6, 2)
    answer.config(text=km)

input = Entry(width=15)
input.grid(row=0, column=1)

miles = Label(text="Miles")
miles.grid(row=0, column=2)
miles.config(padx=15, pady=15)

equal = Label(text='is equal to ')
equal.grid(column=0, row=1)
equal.config(padx=15, pady=15)

answer = Label(text='0')
answer.grid(column=1, row=1)
answer.config(padx=15, pady=15)

unit = Label(text='Km')
unit.grid(column=2, row=1)
unit.config(padx=15, pady=15)

button = Button(text='Calculate', command=convert)
button.grid(column=1, row=2)
button.config(padx=5, pady=5)



window.mainloop()