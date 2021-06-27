import os
import sys
import time
import tkinter
from md5 import *
from threading import Thread
from tkinter import *
from tkinter import ttk

root = Tk()
root.overrideredirect(1)

root.title('Tramell Software Development | Login')
root.iconbitmap('img/icons/favicon.ico')
root.geometry('960x640+380+130')
root.configure(bg='#050505', border=0)
root.resizable(False, False)

BGdock = PhotoImage(file='img/bg/dock.png')
exitIMG = PhotoImage(file='img/icons/exit16x16.png')
exitIMGopace = PhotoImage(file='img/icons/exit16x16opace.png')
hideIMG = PhotoImage(file='img/icons/hide16x16.png')
hideIMGopace = PhotoImage(file='img/icons/hide16x16opace.png')
userIMG = PhotoImage(file='img/icons/user32x32.png')
passIMG = PhotoImage(file='img/icons/pass32x32.png')

world = Canvas(bg='#050505', width=960, height=640, relief='ridge', highlightthickness=0)
world.pack()

DOCK = world.create_image(0, 0, anchor=NW, image=BGdock)
exitBTN = world.create_image(930, 13, anchor=NW, image=exitIMGopace)
hideBTN = world.create_image(900, 13, anchor=NW, image=hideIMGopace)
userEMB = world.create_image(235, 351, anchor=NW, image=userIMG)
passEMB = world.create_image(235, 407, anchor=NW, image=passIMG)

# #0d0d0d

xuserBDR = Label(bg='#050505', width=52, height=2)
xuserBDR.pack()
xuserBDR.place(x=280, y=345)

xuserFLD = Entry(bg='#050505', fg='#ffffff', insertbackground='#c4c4c4', insertwidth=10, width=25, font='{Consolas} 22', border=0, cursor='hand2')
xuserFLD.pack()
xuserFLD.place(x=290, y=350)

xpassBDR = Label(bg='#050505', width=52, height=2)
xpassBDR.pack()
xpassBDR.place(x=280, y=405)

xpassFLD = Entry(bg='#050505', fg='#ffffff', insertbackground='#c4c4c4', insertwidth=10, width=25, font='{Consolas} 22', border=0, cursor='hand2', show='*')
xpassFLD.pack()
xpassFLD.place(x=290, y=410)

def exitAPP(self):

	time.sleep(0.9)
	exitPRCS = Thread(target=root.quit())
	exitPRCS.start()

def hideAPP(self):

	root.overrideredirect(0)
	root.iconify()

def showAPP(self):

	windowSTAT = root.winfo_viewable()

	if windowSTAT == 0:

		root.overrideredirect(0)

	elif windowSTAT == 1:

		time.sleep(0.015)
		root.overrideredirect(1)

def exitBTNhover(self):

	root.config(cursor='hand2')
	world.itemconfig(exitBTN, image=exitIMG)
	world.update()

def exitBTNunhover(self):

	root.config(cursor='arrow')
	world.itemconfig(exitBTN, image=exitIMGopace)
	world.update()

def hideBTNhover(self):

	root.config(cursor='hand2')
	world.itemconfig(hideBTN, image=hideIMG)
	world.update()

def hideBTNunhover(self):

	root.config(cursor='arrow')
	world.itemconfig(hideBTN, image=hideIMGopace)
	world.update()

world.tag_bind(exitBTN, '<Enter>', exitBTNhover)
world.tag_bind(exitBTN, '<Leave>', exitBTNunhover)
world.tag_bind(exitBTN, '<Button-1>', exitAPP)
world.tag_bind(hideBTN, '<Enter>', hideBTNhover)
world.tag_bind(hideBTN, '<Leave>', hideBTNunhover)
world.tag_bind(hideBTN, '<Button-1>', hideAPP)
root.bind('<Escape>', exitAPP)
root.bind('<Enter>', showAPP)
root.bind('<Leave>', showAPP)

xuserFLD.focus()
root.mainloop()