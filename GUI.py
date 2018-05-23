from tkinter import *
import tkinter as tk
import os
import sys
from subprocess import call

root = Tk()
root.title("Extractor")
root.minsize(300,300)
root.geometry("500x500")
thelabel = Label(root,text="Enumeration tool for PCAP")
thelabel.pack()
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
thelabel.pack()
w = tk.Label(root,text = "Please move your previous saved-file (File.csv) this system overwrites",fg = "red",font=("Arial",10))

def quit():
 root.destroy()
def enum():
 call(['bash','callme.sh'])
button1 = Button(bottomFrame,text = "exit",command = quit)
button2 = Button(topFrame, text = "Enumerate",command = enum)
thelabel.pack()
topFrame = Frame(root)
topFrame.pack()
topFrame = Frame(root)
topFrame.pack()
button1.pack()
button2.pack()
w.pack()
root.mainloop()
