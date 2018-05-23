from tkinter import *
import tkinter as tk
import os
import sys
from subprocess import call
root = Tk()
root.title("Extractor")
root.minsize(300,300)
root.geometry("800x800")
thelabel = Label(root,text="Extractor")
thelabel.pack()
thelabel.config(font=("Arial", 44))
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
thelabel.pack()

def quit():
 root.destroy()
button1 = Button(bottomFrame,text = "exit",command = quit)
button1.pack()
root.mainloop()

