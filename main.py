'''
Brooks Farish
Computer Science
10/20/2020
'''
# Python program to create a table
#28 parking (a/b)
#56 spots

from tkinter import *
import tkinter as tk
from tkinter import filedialog
import datetime
master = Tk()

#Main Page
master.title("Parking")
master.geometry("800x800") #box size
master.configure(background="grey90") #GUI Background color

def subMenu(): #Admin Page
    sub = Toplevel(master)
    sub.title("Admin")
    sub.geometry("800x400")  # box size
    sub.configure(background="grey90")  # GUI Background color
    #adminFunc()
#def adminFunc():

    label = tk.Label(sub, text="ADMINISTRATOR",font=("Helvetica", 16))
    label.place(x=330, y=25, height=40, width=180)
    Button(sub, text='Edit CSV', command=entrySave, bg="gray20", fg="white", highlightbackground="gray20",
           activebackground="deep sky blue").place(x=330, y=300, height=40, width=180)
    Button(sub, text='Export CSV', command=black, bg="gray20", fg="white", highlightbackground="gray20",
           activebackground="deep sky blue").place(x=130, y=300, height=40, width=180)
    Button(sub, text='Veiw CSV', command=subMenu, bg="gray20", fg="white", highlightbackground="gray20",
           activebackground="deep sky blue").place(x=530, y=300, height=40, width=180)



#Frames
frame1 = tk.Frame(master, width=750, height=400)
frame2 = tk.Frame(master, width=750, height=400)
frame3 = tk.Frame(master, width=800, height=400)
frame4 = tk.Frame(master, width=800, height=400)

frame1.grid(row=0, column=0)
frame2.grid(row=1, column=0)
frame3.grid(row=1, column=1)
frame4.grid(row=0, column=1)


label = tk.Label(frame1, text="PARKING ID")
entry = tk.Entry(frame1) #input box

label.place(x=330, y=25, height=20, width=80)
entry.place(x=10, y=50, height=300, width=700)


def array():
    spot = 0
    parkingArray = [[spot for i in range(2)] for j in range(28)]
    print(parkingArray)


def entrySave(parkingArray, spot):
    etest = 1
    eSave = entry.get()
    print(eSave)
    parkingArray.append([etest, ])
    #parkingArray.append(eSave)
    print(parkingArray)
    print(spot)


def black():
    frame4 = tk.Frame(master, width=800, height=400, bg="yellow")
    frame4.grid(row=0, column=1)

dayinfo = datetime.datetime.now()

label = tk.Label(frame3, text=dayinfo.strftime("%m/%d/%y - %X"),font=("Helvetica", 28))
label.place(x=200, y=200, height=80, width=400)

#Buttons
Button(frame2, text='Save',command=entrySave, bg="gray20", fg="white", highlightbackground="gray20", activebackground="deep sky blue").place(x=230, y=100, height=60, width=120)

Button(frame2, text='View',command=black, bg="gray20", fg="white", highlightbackground="gray20", activebackground="deep sky blue").place(x=430, y=100, height=60, width=120)

Button(frame2, text='Admin',command=subMenu, bg="gray20", fg="white", highlightbackground="gray20", activebackground="deep sky blue").place(x=330, y=250, height=60, width=120)


array()
master.mainloop()