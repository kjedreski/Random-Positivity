from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from src import app


window = Tk()
window.title("Random Positivity")
window.geometry('50x200')
window.configure(background = "grey");

def start():
   print("start button click")
   app.main()

def stop():
   print("end button click")


a = Button(window ,text="Start",command=start).grid(row = 0,column = 0)
a = Button(window ,text="Stop",command=stop).grid(row = 1,column = 0)

#c = Label(window ,text = "Email Id").grid(row = 2,column = 0)
#c1 = Entry(window).grid(row = 2,column = 1)

def settings():
    print("settings btn clicked")
    pass

btn = ttk.Button(window ,text="Settings",command=settings).grid(row=6,column=0)
window.mainloop()

