#!/usr/bin/python
from tkinter import *
import tkinter
import tkinter.messagebox as tm

top = tkinter.Tk()
top.title("Hashca#c")
top.geometry("600x400")

entry_var = tkinter.StringVar()

entry_label = Label(top, text="Input", font=('calibre',10, 'bold'))


data_entry = Entry(top, textvariable = entry_var, font=('calibre',10,'normal'), bd =5)


def helloCallBack():
   entry = entry_var.get()
   tm.showinfo( "Your Hash", "Your hash is " + entry + ".")

B = tkinter.Button(top, text ="Hash", command = helloCallBack)

entry_label.grid(row=0,column=0)
data_entry.grid(row=0,column=1)
B.grid(row=2,column=1)

# Code to add widgets will go here...
top.mainloop()

