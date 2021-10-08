#from future.moves import tkinter
import tkinter as tk
import random
import string
import sys
import os
from tkinter import *
from tkinter import ttk
from screeninfo import get_monitors
from random import randint
import pyglet, tkinter

root = Tk()
pyglet.font.add_file("/Users/andrestrujillo/Desktop/Snellen.ttf") #Path fo file then add .ttf
#root.geometry("2560x1600")
root.geometry("1920x1080")
#changing the size of letters--> Pop up window
global entry
global pop
resizedFont = 1
factor = 1
distanceFactor = 1

def popUp():
    def save():
        global factor
        global resizedFont
        resizedFont = float(entry.get())
        conversion = float(resizedFont*0.393701)
        #print(resizedFont)
        factor = 1.7452756/conversion
        print(factor)
    pop = Toplevel(root)
    pop.title('Resize Characters')
    pop.geometry("500x350")
    explanation = Label(pop, text = "Measure and input the height(in cm) of the letter below").pack()
    Letter = Label(pop, text = "E", font = "Snellen 126").pack()#the 20/20 size for 100 feet #real size is 1.7452756
    entry = Entry(pop, width = 5)
    entry.pack()
    save = Button(pop, text = "Save", command = save).pack()

windowButton = Button(root, text = 'Resize Characters', command = popUp).pack()

def popUpDistance():
    def save():
        global distance
        global distanceFactor
        distance = float(entry.get())
        print(distance)

        distanceFactor = (distance * 25.2)/20
        distanceFactor = 25.2/distance
        print(distanceFactor)

    pop = Toplevel(root)
    pop.title('Input Distance')
    pop.geometry("400x200")
    explanation = Label(pop, text = "Input the distance (in feet) the patient is from the chart").pack()
    entry = Entry(pop, width = 5)
    entry.pack()
    save = Button(pop, text = "Save", command = save).pack()


windowButton = Button(root, text = 'Input Distance', command = popUpDistance).pack()

#Scrollbar
main_frame = Frame(root)
main_frame.pack(fill = BOTH, expand = 1)
my_canvas = Canvas(main_frame)
my_canvas.pack(side = LEFT, fill = BOTH, expand = 1)
my_scrollbar = ttk.Scrollbar(main_frame, orient = VERTICAL, command = my_canvas.yview)
my_scrollbar.pack(side = RIGHT, fill = Y)
my_canvas.configure(yscrollcommand = my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
second_frame = Frame(my_canvas)
my_canvas.create_window((0,0), window = second_frame, anchor = 'nw')

def change_text():
    line0.config(text=random.choice(string.ascii_uppercase), font ="Snellen " + str(round(1.28*504*factor/distanceFactor)))
    line1.config(text=random.choice(string.ascii_uppercase), font ="Snellen " + str(round(1.28*252*factor/distanceFactor)))
    line2.config(font ="Snellen " + str(round(1.28*126*factor/distanceFactor)), text=random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase))
    line3.config(font ="Snellen " + str(round(1.28*88*factor/distanceFactor)), text=random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase))
    line4.config(font ="Snellen " + str(round(1.28*99*factor/distanceFactor)), text=random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase))
    line5.config(font ="Snellen " + str(round(1.28*88*factor/distanceFactor)), text=random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase))
    line6.config(font ="Snellen " + str(round(1.28*74*factor/distanceFactor)), text=random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase) + "  " +random.choice(string.ascii_uppercase))
    line7.config(font ="Snellen " + str(round(1.28*50*factor/distanceFactor)), text=random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase))
    line8.config(font ="Snellen " + str(round(1.28*38*factor/distanceFactor)), text=random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase))
    line9.config(font ="Snellen " + str(round(1.28*31*factor/distanceFactor)), text=random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase)+ "  " + random.choice(string.ascii_uppercase))
    line10.config(font ="Snellen " + str(round(1.28*25*factor/distanceFactor)), text=random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase)+ "  " + random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase))
    line11.config(font ="Snellen " + str(round(1.28*13*factor/distanceFactor)), text=random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase)+ "  " + random.choice(string.ascii_uppercase)+ "  " + random.choice(string.ascii_uppercase)+ "  " + random.choice(string.ascii_uppercase))
def change_to_number():
    line0.config(font ="Snellen " + str(round(504*factor/distanceFactor)), text=randint(0,9))
    line1.config(font ="Snellen " + str(round(252*factor/distanceFactor)), text=randint(0,9))
    line2.config(font ="Snellen " + str(round(126*factor/distanceFactor)), text=str(randint(0,9)) + "  " + str(randint(0,9)))
    line3.config(font ="Snellen " + str(round(88*factor/distanceFactor)), text=str(randint(0,9)) + "  " + str(randint(0,9)) + "  " + str(randint(0,9)))
    line4.config(font ="Snellen " + str(round(63*factor/distanceFactor)), text=str(randint(0,9)) + "  " + str(randint(0,9)) + "  " + str(randint(0,9)) + "  " + str(randint(0,9)))
    line5.config(font ="Snellen " + str(round(50*factor/distanceFactor)), text=str(randint(0,9)) + "  " + str(randint(0,9)) + "  " + str(randint(0,9)) + "  " + str(randint(0,9)) + "  " + str(randint(0,9)))
    line6.config(font ="Snellen " + str(round(38*factor/distanceFactor)), text=str(randint(0,9)) + "  " + str(randint(0,9)) + "  " + str(randint(0,9)) + "  " + str(randint(0,9)) + "  " + str(randint(0,9)) + "  " + str(randint(0,9)))
    line7.config(font ="Snellen " + str(round(31*factor/distanceFactor)), text=str(randint(0,9)) + "  " + str(randint(0,9)) + "  " + str(randint(0,9)) + "  " + str(randint(0,9)) + "  " + str(randint(0,9)) + "  " + str(randint(0,9)) + "  " + str(randint(0,9)))
    line8.config(font ="Snellen " + str(round(25*factor/distanceFactor)), text=str(randint(0,9)) + "  " + str(randint(0,9)) + "  " + str(randint(0,9)) + "  " + str(randint(0,9)) + "  " + str(randint(0,9)) + "  " + str(randint(0,9)) + "  " + str(randint(0,9)) + "  " + str(randint(0,9)))
    line9.config(font ="Snellen " + str(round(13*factor/distanceFactor)), text=str(randint(0,9)) + "  " + str(randint(0,9)) + "  " + str(randint(0,9)) + "  " + str(randint(0,9)) + "  " + str(randint(0,9)) + "  " + str(randint(0,9)) + "  " + str(randint(0,9)) + "  " + str(randint(0,9))+ "  " + str(randint(0,9)))

button= Button(root, text='Change Letters!', command=change_text)
button.pack()

button2 = Button(root, text = "Change Numbers!", command = change_to_number)
button2.pack()
line0 = Label(second_frame, text=random.choice(string.ascii_uppercase), font="Snellen 504", highlightthickness = 0)#20/400
line1 = Label(second_frame, text=random.choice(string.ascii_uppercase), font="Snellen 252")#20/200
line2 = Label(second_frame, text=random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase), font="Snellen 126")#20/100
line3 = Label(second_frame, text=random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase), font="Snellen 99")#20/80
line4 = Label(second_frame, text=random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase), font="Snellen 88")#20/70
line5 = Label(second_frame, text=random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase), font="Snellen 74")#20/60
line6 = Label(second_frame, text=random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase) + "  " +random.choice(string.ascii_uppercase), font="Snellen 63")#20/50
line7 = Label(second_frame, text=random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase), font="Snellen 50") #20/40
line8 = Label(second_frame, text=random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase) + "  "+ random.choice(string.ascii_uppercase), font="Snellen 38") #20/30
line9 = Label(second_frame, text=random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase)+ "  " + random.choice(string.ascii_uppercase), font="Snellen 31")#20/25
line10 = Label(second_frame, text=random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase)+ "  " + random.choice(string.ascii_uppercase) + " " + random.choice(string.ascii_uppercase), font="Snellen 25") #20/20
line11 = Label(second_frame, text=random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase) + "  " + random.choice(string.ascii_uppercase)+ "  " + random.choice(string.ascii_uppercase)+ " " + random.choice(string.ascii_uppercase)+ " " + random.choice(string.ascii_uppercase), font="Snellen 19") #20/15

SizeLabel0 = Label(second_frame, text= "20/400")
SizeLabel1 = Label(second_frame, text= "20/200")
SizeLabel2 = Label(second_frame, text= "20/100")
SizeLabel3 = Label(second_frame, text= "20/80")
SizeLabel4 = Label(second_frame, text= "20/70")
SizeLabel5 = Label(second_frame, text= "20/60")
SizeLabel6 = Label(second_frame, text= "20/50")
SizeLabel7 = Label(second_frame, text= "20/40")
SizeLabel8 = Label(second_frame, text= "20/30")
SizeLabel9 = Label(second_frame, text= "20/25")
SizeLabel10 = Label(second_frame, text= "20/20")
SizeLabel11 = Label(second_frame, text= "20/15")




blank1 = Label(second_frame, text=" ", font = 'Courier 150')
blank2 = Label(second_frame, text=" ", font = 'Courier 150')
blank3 = Label(second_frame, text=" ", font = 'Courier 150')
blank4 = Label(second_frame, text=" ", font = 'Courier 150')
blank5 = Label(second_frame, text=" ", font = 'Courier 150')
blank6 = Label(second_frame, text=" ", font = 'Courier 150')
blank7 = Label(second_frame, text=" ", font = 'Courier 150')
blank8 = Label(second_frame, text=" ", font = 'Courier 150')
blank9 = Label(second_frame, text=" ", font = 'Courier 150')
blank10 = Label(second_frame, text=" ", font = 'Courier 150')
blank11 = Label(second_frame, text=" ", font = 'Courier 150')

blank1.grid(row = 1, column = 0, padx= 235)
blank2.grid(row = 3, column = 1, pady=10)
blank3.grid(row = 5, column = 2, pady=10)
blank4.grid(row = 7, column = 3, pady =10)
blank5.grid(row = 9, column = 0, padx= 235)
blank6.grid(row = 11, column = 1, pady=10)
blank7.grid(row = 13, column = 2, pady=10)
blank8.grid(row = 15, column = 3, pady =10)
blank9.grid(row = 17, column = 3, pady =10)
blank10.grid(row = 19, column = 3, pady =10)
blank11.grid(row = 21, column = 3, pady =10)

line0.grid(row = 0, column =1)
line1.grid(row = 2, column =1, pady=20)
line2.grid(row = 4, column =1, pady=10)
line3.grid(row = 6, column =1, pady=10)
line4.grid(row = 8, column =1, pady=10)
line5.grid(row = 10, column =1, pady=10)
line6.grid(row = 12, column =1, pady=10)
line7.grid(row = 14, column =1, pady=10)
line8.grid(row = 16, column =1, pady=10)
line9.grid(row = 18, column =1, pady=10)
line10.grid(row = 20, column =1, pady=10)
line11.grid(row = 22, column =1, pady=10)


SizeLabel0.grid(row = 0, column =2)
SizeLabel1.grid(row = 2, column =2, pady=20)
SizeLabel2.grid(row = 4, column =2, pady=10)
SizeLabel3.grid(row = 6, column =2, pady=10)
SizeLabel4.grid(row = 8, column =2, pady=10)
SizeLabel5.grid(row = 10, column =2, pady=10)
SizeLabel6.grid(row = 12, column =2, pady=10)
SizeLabel7.grid(row = 14, column =2, pady=10)
SizeLabel8.grid(row = 16, column =2, pady=10)
SizeLabel9.grid(row = 18, column =2, pady=10)
SizeLabel10.grid(row = 20, column=2, pady=10)
SizeLabel11.grid(row = 22, column=2, pady =10)


root.mainloop()

