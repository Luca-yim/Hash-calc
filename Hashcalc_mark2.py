from tkinter import *
import tkinter
import tkinter.messagebox as tm
import math

# setting the windows size and title
top = tkinter.Tk()
top.title("Hashca#c")
top.geometry("600x400")

# declaring string variable
# for storing data entry
entry_var = tkinter.StringVar()

# creating a label for
# data input using widget Label
entry_label = Label(top, text="Input", font=('calibre',10, 'bold'))

# creating an entry for data
# input using widget Entry
data_entry = Entry(top, textvariable = entry_var, font=('calibre',10,'normal'), bd =5)

# defining a function that will
# get the data input, hash it and
# print them on the screen
def hashCallBack():
   entry = entry_var.get()
   
   #changing string to number
   x = range(len(entry))
   i = 0
   for n in x:
       i = ord(entry[n]) + i
   data_num = i
   
   #using multiplication method to hash entry
   A = 0.2072002
   M = 100
   rep = math.floor(M * (data_num * A % 1))
   tm.showinfo( "Your Hash", "Your hash is " + str(rep) + ".")

# creating a button using the widget
# Button that will call the hashCallBack function
B = tkinter.Button(top, text ="Hash", command = hashCallBack)

# placing the label and entry in
# the required position using grid
# method
entry_label.grid(row=0,column=0)
data_entry.grid(row=0,column=1)
B.grid(row=2,column=1)

# performing an infinite loop
# for the window to display
top.mainloop()
