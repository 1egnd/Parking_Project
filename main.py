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
from tkinter import messagebox
import time
import re
import smtplib, ssl #email
from os import startfile
from time import strftime
master = Tk()

#Main Page
master.title("Parking") #Window Title
master.geometry("1920x1080") #Window size
master.configure(background="grey90") #GUI background color

#Function that builds the Profile page sub menu
global entryUser
def subMenu():
    sub = Toplevel(master)
    sub.title("Profile") #Sub menu title
    sub.geometry("800x400")  #Sub menu size
    sub.configure(background="grey90")  # GUI background color
#Profile page labels
    label = tk.Label(sub, text="Contact",font=("Helvetica", 16))
    label.place(x=330, y=25, height=40, width=180)
    label = tk.Label(sub, text="Name") # Username Label
    label.place(x=250, y=100, height=30, width=60)
    label = tk.Label(sub, text="Email") # Password Label
    label.place(x=250, y=150, height=30, width=60)

    global entryUser
    entryUser = tk.Entry(sub)
    entryUser.place(x=330, y=100, height=30, width=180)
    global entryEmail
    entryEmail = tk.Entry(sub)
    entryEmail.place(x=330, y=150, height=30, width=180)
    save = entryUser.get()
# Profile page buttons
    Button(sub, text='Edit/Veiw  Users',command=editText,  bg="gray20", fg="white", highlightbackground="gray20",
           activebackground="deep sky blue").place(x=230, y=300, height=40, width=180)  # CSV Edit Button /open file
    Button(sub, text='Upload User', command=saveText, bg="gray20", fg="white", highlightbackground="gray20",
           activebackground="deep sky blue").place(x=430, y=300, height=40, width=180)  # CSV Veiw Button /saveText

#Function that save user profiles to .txt
def saveText():
    username = entryUser.get() #Pulls username from entry box
    email = entryEmail.get() #Pulls email from entry box
    userdata = username +", " +email #Writing into txt format
    writeTo = open("ParkingUsers.txt", 'a') #'a' is append to add to doc vs w to overwrite
    writeTo.write(userdata +"\n") #write and indent for next user
    print(userdata)
    writeTo.close()


def editText():
    startfile("ParkingUsers.txt")


#Frames
frame1 = tk.Frame(master, width=750, height=400, background="grey90") #Section of GUI
frame2 = tk.Frame(master, width=750, height=400, background="grey90") #Section of GUI
frame3 = tk.Frame(master, width=800, height=400, background="grey90") #Section of GUI
frame4 = tk.Frame(master, width=800, height=400, background="grey90") #Section of GUI

frame1.grid(row=0, column=0)
frame2.grid(row=1, column=0)
frame3.grid(row=1, column=1)
frame4.grid(row=0, column=1)


label = tk.Label(frame1, text="PARKING ID",font=("Helvetica", 16)) #Parking ID Label
entry = tk.Entry(frame1,justify='center',font=("Helvetica", 60)) #Main entry box
Nameentry = tk.Entry(frame1,justify='center',font=("Helvetica", 14)) #Main name entry box
Namelabel = tk.Label(frame1, text="Name",font=("Helvetica", 12)) #Name label
Emaillentry = tk.Entry(frame1,justify='center',font=("Helvetica", 14)) #Main name entry box
Emaillabel = tk.Label(frame1, text="Ask to move! Email:",font=("Helvetica", 12)) #Name label

# Entry and Label Locations
label.place(x=320, y=25, height=20, width=125) #Location of Parking ID text label
entry.place(x=20, y=50, height=170, width=700) #Location of entry box for Parking ID

Nameentry.place(x=20, y=260, height=50, width=700) #Location for Name text entry
Namelabel.place(x=360, y=235, height=20, width=50) #Location for Name text label

Emaillentry.place(x=20, y=355, height=50, width=700) #Location for Email text entry
Emaillabel.place(x=310, y=330, height=20, width=150) #Location for Email text label

#Parking spot buttons red and green on click functionality
toggle = []
def start(spotNum):
    entry.delete(0,100)
    entry.insert(0,parkingSpotsArray[spotNum])
    if toggle [spotNum] == "g":
        spots[spotNum].configure(relief=tk.SUNKEN, bg="red") #Buttons red on indent click
        toggle[spotNum] = "r"
    else:
        entry.delete(0, 100)
        spots[spotNum].configure(relief=tk.RAISED, bg="green") #Buttons green on extrude click
        toggle[spotNum] = "g"


#Array that builds parking spot buttons
spots = []
parkingSpotsArray = []
keypadCounter = 0 #Making variable empty
for i in range(1, 29): #start at one and give 29 spots
    for j in range(0, 2):
        if j == 0:
            letter = "A"
        else:
            letter = "B"
        parkingSpotz = str(i) + letter
        arraySpot = Button(frame4, text=parkingSpotz, command=lambda keypadCounter=keypadCounter:
        start(keypadCounter), bg="green", fg="black", highlightbackground="black", activebackground="red", relief=FLAT, height=9, width=2)
        arraySpot.grid(row=j, column=i, pady=5, padx=1)
        parkingSpotsArray.append(parkingSpotz)
        spots.append(arraySpot)
        toggle.append("g") #green
        keypadCounter = keypadCounter + 1

def array():
    spot = 0
    global parkingArray
    parkingArray = [["empty" for i in range(3)] for j in range(56)]
    print(parkingArray)
    global userInfo
    userInfo = [["userNull" for i in range(3)] for j in range(2)]
    print(userInfo)


def entrySave(): #Parking Spot I.D Saving Logic
    eSave = (entry.get()) #Taking string from input box on save press #Nameentry.get()
    res = [re.findall(r'(\d+)(\w+?)', eSave)[0] ]
    print(res)
    print(res[0][0])
    print(res[0][1])
    intElement = int(res[0][0])
    name = (Nameentry.get())

    parkingArray[intElement][2] =  res[0][1]
    parkingArray[intElement][1] = intElement
    parkingArray[intElement][0] = name
    print(parkingArray)

#Function for veiw button showing selected spot occupier name
def veiw():
    eSave = (entry.get())  # Taking string from input box on save press #Nameentry.get()
    res = [re.findall(r'(\d+)(\w+?)', eSave)[0]]
    intElement = int(res[0][0])
    Name = (parkingArray[intElement][0])
    print(Name)
    print("in view")
    print(res[0][1])
    print(type(res[0][1]))
    stringEx = res[0][1]
    if ((stringEx == "a" and "A" or stringEx == "b" and "B" )): #error hand
        print("ok")
        namePop(Name)
    else:
        messagebox.showinfo("Error", " Invalid Spot")

#Function for name pop up window
def namePop(Name):
    messagebox.showinfo("Name", Name)


def counter_label(label):
    counter = 0

    def count():
        global counter
        counter += 1
        label.config(text=str(counter))
        label.after(1000, count)
    count()

# This function is used to display time on the label
def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)

# Styling the label widget so that clock will look more attractive
lbl = Label(frame3, font=('calibri', 40, 'bold'),
            background='grey',
            foreground='white')
lbl.pack(anchor='center')

#Function that sends email asking occupier to move his car
def sendMail():
    emailGet = (Emaillentry.get())
    SUBJECT = "Car Bot Notification - Do Not Reply"

    TEXT = "Please Move Your Car!"
    message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("parkingpostoaknoreply" , "!Postoakparking1")
    server.sendmail(emailGet,emailGet, message) #message
    server.quit()


#Buttons
Button(frame2, text='Save',command=entrySave, bg="gray20", fg="white", highlightbackground="gray20", activebackground="deep sky blue").place(x=230, y=100, height=60, width=120)

Button(frame2, text='View',command=veiw, bg="gray20", fg="white", highlightbackground="gray20", activebackground="deep sky blue").place(x=430, y=100, height=60, width=120)

Button(frame2, text='Send Email',command=sendMail, bg="gray20", fg="white", highlightbackground="gray20", activebackground="deep sky blue").place(x=230, y=250, height=60, width=120)

Button(frame2, text='Profile',command=subMenu, bg="gray20", fg="white", highlightbackground="gray20", activebackground="deep sky blue").place(x=430, y=250, height=60, width=120)

time()
array()
master.mainloop()