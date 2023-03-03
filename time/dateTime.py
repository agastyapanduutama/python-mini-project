from tkinter import *
from tkinter.ttk import *
from time import strftime
from datetime import date


waktos = Tk()
tanggal = Tk()

waktos.title("Jam")
tanggal.title("Tanggal")

def clock():
    tick = strftime("%H:%M:%S %p")
    label.config(text=tick)
    label.after(1000, clock)

def tanggalNa():
    ticktanggal = date.today()
    label2.config(text=ticktanggal)
    label2.after(1000, clock)


# Use label method to store our title.
label =  Label(waktos, font=("segoe", 60), foreground="white", background="black")
label2 = Label(tanggal, font=("segoe", 60), foreground="white", background="black")

label.pack(anchor="center")
label2.pack(anchor="center")

# Call our clock function and at the end we will call it mainloop
tanggalNa()
clock()
mainloop()
