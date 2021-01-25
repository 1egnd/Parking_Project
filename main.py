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
from tkinter import messagebox
import datetime
import time
import re
import smtplib #email
import smtplib, ssl #email
from os import startfile
from time import strftime
master = Tk()

#Main Page
master.title("Parking") #Window Title
master.geometry("1920x1080") #Box size (1920x1080 but small for test)
master.configure(background="grey90") #GUI Background color




'''
def emailSend(): #parkingpostoaknoreply@gmail.com #!Postoakparking1

    sender = 'from@fromdomain.com'
    receivers = ['to@todomain.com']

    message = """From: From Person <from@fromdomain.com>
    To: To Person <to@todomain.com>
    Subject: SMTP e-mail test

    This is a test e-mail message.
    """

    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message)
    print("Successfully sent email")
'''




global entryUser
def subMenu(): #Admin Page
    sub = Toplevel(master)
    sub.title("Admin")
    sub.geometry("800x400")  # box size
    sub.configure(background="grey90")  # GUI Background color
#admin buttons
    label = tk.Label(sub, text="Contact",font=("Helvetica", 16))
    label.place(x=330, y=25, height=40, width=180)
    label = tk.Label(sub, text="Name") # Username Label
    label.place(x=250, y=100, height=30, width=60)
    label = tk.Label(sub, text="Email") # Password Label
    label.place(x=250, y=150, height=30, width=60)

    global entryUser
    entryUser = tk.Entry(sub)  # Name input box #did not use textvariable=userGet
    entryUser.place(x=330, y=100, height=30, width=180)
    global entryEmail
    entryEmail = tk.Entry(sub)  # Email input box #did not use textvariable=emailGet
    entryEmail.place(x=330, y=150, height=30, width=180)
    save = entryUser.get()
    Button(sub, text='Edit Users',command=editText,  bg="gray20", fg="white", highlightbackground="gray20",
           activebackground="deep sky blue").place(x=230, y=300, height=40, width=180)  # CSV Edit Button /open file
    Button(sub, text='Upload User', command=saveText, bg="gray20", fg="white", highlightbackground="gray20",
           activebackground="deep sky blue").place(x=430, y=300, height=40, width=180)  # CSV Veiw Button /saveText

def saveText():
    print("Here")
    username = entryUser.get()
    email = entryEmail.get()
    userdata = username +", " +email
    writeTo = open("ParkingUsers.txt", 'a') #'a' is append to add to doc vs w to overwrite
    writeTo.write(userdata +"\n")
    print(userdata)
    writeTo.close()


def editText():
    print("here!!")
    startfile("ParkingUsers.txt")


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
entry = tk.Entry(frame1,justify='center',font=("Helvetica", 60)) #Main entry box
Nameentry = tk.Entry(frame1,justify='center',font=("Helvetica", 14)) #Main name entry box
Namelabel = tk.Label(frame1, text="Name",font=("Helvetica", 12)) #Name label

label.place(x=320, y=25, height=20, width=120)
entry.place(x=20, y=50, height=270, width=700) #was 300
Nameentry.place(x=20, y=355, height=50, width=700)
Namelabel.place(x=320, y=330, height=20, width=120)

toggle = []
def start(spotNum):
    entry.delete(0,100)
    entry.insert(0,parkingSpotsArray[spotNum])
    if toggle [spotNum] == "g":
        spots[spotNum].configure(relief=tk.SUNKEN, bg="red")
        toggle[spotNum] = "r"
    else:
        entry.delete(0, 100)
        spots[spotNum].configure(relief=tk.RAISED, bg="green")
        toggle[spotNum] = "g"

#counter
spots = []
parkingSpotsArray = []
keypadCounter = 0
for i in range(1, 29): #start at one and give 29 spots
    for j in range(0, 2):
        if j == 0:
            letter = "A"
        else:
            letter = "B"
        parkingSpotz = str(i) + letter
        #print(parkingSpotz)
        #print(i, ' ', letter, " ")
        arraySpot = Button(frame4, text=parkingSpotz, command=lambda keypadCounter=keypadCounter: start(keypadCounter), bg="green", fg="black", highlightbackground="grey20", activebackground="red", relief=FLAT)
        arraySpot.grid(row=j, column=i)
        parkingSpotsArray.append(parkingSpotz)
        #print(arraySpot)
        spots.append(arraySpot)
        print(spots)
        toggle.append("g") #green
        keypadCounter = keypadCounter + 1
#print(spots)

def array():
    spot = 0
    global parkingArray
    parkingArray = [["empty" for i in range(3)] for j in range(56)]
    parkingArray [0][0] = "mike"
    parkingArray [0][1] = "mike@gmail.com"
    parkingArray [1][0] = "john"
    parkingArray [1][1] = "john@gmail.com"
    #make if statement that check array for val of 0 then make gui button green
    print(parkingArray)
    #parkingArrayVisitor = [["" for i in range(2)] for j in range(28)]
    global userInfo
    userInfo = [["userNull" for i in range(3)] for j in range(2)]
    print(userInfo)


def entrySave(): #Parking Spot I.D Saving Logic
    etest = 1
    eSave = (entry.get()) #Taking string from input box on save press #Nameentry.get()
    res = [re.findall(r'(\d+)(\w+?)', eSave)[0] ]
    print(res)
    print(res[0][0])
    print(res[0][1])
    #print(res[0][2])
    intElement = int(res[0][0])
    name = (Nameentry.get())

    parkingArray[intElement][2] =  res[0][1]
    parkingArray[intElement][1] = intElement
    parkingArray[intElement][0] = name
    print(parkingArray)

def veiw(): #CHANGE TO VIEW
    try:
        eSave = (entry.get())  # Taking string from input box on save press #Nameentry.get()
        res = [re.findall(r'(\d+)(\w+?)', eSave)[0]]
        intElement = int(res[0][0])
        Name = (parkingArray[intElement][0])
    except IndexError:
        messagebox.showinfo("Error", " Invalid Spot")
    namePop(Name)

def namePop(Name):
    messagebox.showinfo("Name", Name)

dayinfo = datetime.datetime.now() #Date and time defined text=dayinfo.strftime("%m/%d/%y - %X") font=("Helvetica", 28)

dateinfo = tk.Entry(frame3,font=("Helvetica", 28)) #Date and time label (% is formating)
dateinfo.place(x=200, y=200, height=80, width=400)

dateinfo.insert(tk.INSERT, dayinfo.strftime("%m/%d/%y - %X"))
#print(dayinfo.strftime("%m/%d/%y - %X"))

counter = 0

def counter_label(label):
    counter = 0

    def count():
        global counter
        counter += 1
        label.config(text=str(counter))
        label.after(1000, count)
    count()

# This function is used to
# display time on the label
def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)

# Styling the label widget so that clock
# will look more attractive
lbl = Label(frame3, font=('calibri', 40, 'bold'),
            background='grey',
            foreground='white') #CHANGE TO WHITE TO FIX COLOR ISSUE
lbl.pack(anchor='center')

def send_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("username without @gmail.com", "password")
    server.sendmail(
        "from@gmail.com",
        "to @ post oak.com",
        "this message is from python--2")
    server.quit()


#Buttons
Button(frame2, text='Save',command=entrySave, bg="gray20", fg="white", highlightbackground="gray20", activebackground="deep sky blue").place(x=230, y=100, height=60, width=120)

Button(frame2, text='View',command=veiw, bg="gray20", fg="white", highlightbackground="gray20", activebackground="deep sky blue").place(x=430, y=100, height=60, width=120)

Button(frame2, text='Send SMS',command=send_mail, bg="gray20", fg="white", highlightbackground="gray20", activebackground="deep sky blue").place(x=230, y=250, height=60, width=120)

Button(frame2, text='Profile',command=subMenu, bg="gray20", fg="white", highlightbackground="gray20", activebackground="deep sky blue").place(x=430, y=250, height=60, width=120)

time()
array()
master.mainloop()