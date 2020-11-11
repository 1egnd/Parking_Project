'''
Brooks Farish
Computer Science
10/20/2020
'''
# Python program to create a table
#28 parking (a/b)
#56 spots
#add admin add user/ edit users

from tkinter import *
import tkinter as tk
from tkinter import filedialog
import datetime
import re
master = Tk()

#Main Page
master.title("Parking") #Window Title
master.geometry("800x800") #Box size
master.configure(background="grey90") #GUI Background color

def subMenu(): #Admin Page
    sub = Toplevel(master)
    sub.title("Admin")
    sub.geometry("800x400")  # box size
    sub.configure(background="grey90")  # GUI Background color
    #adminFunc()
#def adminFunc():

#admin buttons
    label = tk.Label(sub, text="ADMINISTRATOR",font=("Helvetica", 16))
    label.place(x=330, y=25, height=40, width=180)
    label = tk.Label(sub, text="Username") # Username Label
    label.place(x=250, y=100, height=30, width=60)
    label = tk.Label(sub, text="Password") # Password Label
    label.place(x=250, y=150, height=30, width=60)
    entryUser = tk.Entry(sub)  # Username input box
    entryUser.place(x=330, y=100, height=30, width=180)
    entryPas = tk.Entry(sub)  # Password input box
    entryPas.place(x=330, y=150, height=30, width=180)
    Button(sub, text='Edit CSV', command=entrySave, bg="gray20", fg="white", highlightbackground="gray20",
           activebackground="deep sky blue").place(x=330, y=300, height=40, width=180) #CSV Edit Button
    Button(sub, text='Export CSV', command=black, bg="gray20", fg="white", highlightbackground="gray20",
           activebackground="deep sky blue").place(x=130, y=300, height=40, width=180) #CSV Export Button
    Button(sub, text='Veiw CSV', command=subMenu, bg="gray20", fg="white", highlightbackground="gray20",
           activebackground="deep sky blue").place(x=530, y=300, height=40, width=180) #CSV Veiw Button



#Frames
frame1 = tk.Frame(master, width=750, height=400)
frame2 = tk.Frame(master, width=750, height=400)
frame3 = tk.Frame(master, width=800, height=400)
frame4 = tk.Frame(master, width=800, height=400)

frame1.grid(row=0, column=0)
frame2.grid(row=1, column=0)
frame3.grid(row=1, column=1)
frame4.grid(row=0, column=1)


label = tk.Label(frame1, text="PARKING ID",font=("Helvetica", 16)) #Parking ID Label
entry = tk.Entry(frame1) #Main entry box

label.place(x=320, y=25, height=20, width=120)
entry.place(x=10, y=50, height=300, width=700)


def array():
    spot = 0
    global parkingArray
    parkingArray = [["empty" for i in range(3)] for j in range(56)]
    parkingArray [0][0] = "mike"
    parkingArray [0][1] = "MIKE@G"
    parkingArray [1][0] = "john"
    parkingArray [1][1] = "john@G"
    #make if statement that check array for val of 0 then make gui button green
    print(parkingArray)
    #parkingArrayVisitor = [["" for i in range(2)] for j in range(28)]


def entrySave():
    etest = 1
    eSave = (entry.get()) #Taking string from input box on save press
    res = [re.findall(r'(\d+)(\w+?)', eSave)[0] ]
    print(res)
    print(res[0][0])
    print(res[0][1])
    intElement = int(res[0][0])

    parkingArray[intElement][1] = res[0][1]
    print(parkingArray)
    '''

    #map_elist =
    print(eSave)


    #print(eSave[1])
    parkingArray [eSave] [1] = "bla"
    #parkingArray [1] [0] = eSave
    #parkingArray.append(eSave)
    print(parkingArray)
    #print(spot)

    '''

def black():
    frame4 = tk.Frame(master, width=800, height=400, bg="yellow")
    frame4.grid(row=0, column=1)

dayinfo = datetime.datetime.now() #Date and time defined

label = tk.Label(frame3, text=dayinfo.strftime("%m/%d/%y - %X"),font=("Helvetica", 28)) #Date and time label (% is formating)
label.place(x=200, y=200, height=80, width=400)

#Buttons
Button(frame2, text='Save',command=entrySave, bg="gray20", fg="white", highlightbackground="gray20", activebackground="deep sky blue").place(x=230, y=100, height=60, width=120)

Button(frame2, text='View',command=black, bg="gray20", fg="white", highlightbackground="gray20", activebackground="deep sky blue").place(x=430, y=100, height=60, width=120)

Button(frame2, text='Admin',command=subMenu, bg="gray20", fg="white", highlightbackground="gray20", activebackground="deep sky blue").place(x=330, y=250, height=60, width=120)


array()
master.mainloop()