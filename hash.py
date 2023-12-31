from Utils.helper import b2Tob16, preprocessMessage, chunker, initializer
from Utils.utils import *
from Utils.constants import *
from tkinter import *
import tkinter
import tkinter.messagebox as tm
import math


def sha256(message): 
    
    #initializing some buffer values
    # hard-coded constants representing hash values
    k = initializer(K)
    h0, h1, h2, h3, h4, h5, h6, h7 = initializer(h_hex)
    chunks = preprocessMessage(message)
    
    #Compression function
    for chunk in chunks:
        w = chunker(chunk, 32)
        for _ in range(48):
            w.append(32 * [0])
        for i in range(16, 64):
            s0 = XORXOR(rotr(w[i-15], 7), rotr(w[i-15], 18), shr(w[i-15], 3) ) 
            s1 = XORXOR(rotr(w[i-2], 17), rotr(w[i-2], 19), shr(w[i-2], 10))
            w[i] = add(add(add(w[i-16], s0), w[i-7]), s1)
        a = h0
        b = h1
        c = h2
        d = h3
        e = h4
        f = h5
        g = h6
        h = h7
        for j in range(64):
            S1 = XORXOR(rotr(e, 6), rotr(e, 11), rotr(e, 25) )
            ch = XOR(AND(e, f), AND(NOT(e), g))
            temp1 = add(add(add(add(h, S1), ch), k[j]), w[j])
            S0 = XORXOR(rotr(a, 2), rotr(a, 13), rotr(a, 22))
            m = XORXOR(AND(a, b), AND(a, c), AND(b, c))
            temp2 = add(S0, m)
            h = g
            g = f
            f = e
            e = add(d, temp1)
            d = c
            c = b
            b = a
            a = add(temp1, temp2)
        h0 = add(h0, a)
        h1 = add(h1, b)
        h2 = add(h2, c)
        h3 = add(h3, d)
        h4 = add(h4, e)
        h5 = add(h5, f)
        h6 = add(h6, g)
        h7 = add(h7, h)
    digest = ''
    for val in [h0, h1, h2, h3, h4, h5, h6, h7]:
        digest += b2Tob16(val)
    return digest

        
        
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
   
   tm.showinfo( "Your Hash", "Your hash is : \n" + sha256(entry))

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
