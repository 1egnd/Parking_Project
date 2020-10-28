'''
Brooks Farish
9/25/2020
2nd array
text formatting
read/write text docs
'''
# Python program to create a table

from tkinter import *
import tkinter as tk
from tkinter import filedialog
master = Tk()

master.title("Parking")
master.geometry("800x800") #box size
master.configure(background="grey90") #GUI Background color

frame1 = tk.Frame(master, width=750, height=400, bg="red")
frame2 = tk.Frame(master, width=750, height=400, bg="green")
frame3 = tk.Frame(master, width=800, height=400, bg="blue")
frame4 = tk.Frame(master, width=800, height=400, bg="black")

frame1.grid(row=0, column=0)
frame2.grid(row=1, column=0)
frame3.grid(row=1, column=1)
frame4.grid(row=0, column=1)


label = tk.Label(frame1, text="PARKING ID")
entry = tk.Entry(frame1,)

label.grid(row=0, column=0)
entry.grid(row=1, column=0)


#Buttons
Button(frame2, text='Save', bg="gray20", fg="white", highlightbackground="gray20", activebackground="deep sky blue").grid(row=2, column=1)

Button(frame2, text='View', bg="gray20", fg="white", highlightbackground="gray20", activebackground="deep sky blue").grid(row=2, column=0)

Button(frame2, text='Admin', bg="gray20", fg="white", highlightbackground="gray20", activebackground="deep sky blue").grid(row=2, column=2)



master.mainloop()