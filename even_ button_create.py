"""
Project:Tkinter Event-Driven Button Handling 
Purpose:Demonstrates handling user button click events and executing callback functions in a Tkinter GUI.
Key Concepts:Event-Driven Programming,Command Callback Functions,Pack Layout Manager,Widget Styling (fg/bg).
Usage:Serves as a fundamental template for triggering application logic and actions upon user button Clicks.
"""
from tkinter import *#import all definitions from tkinter

def processOK():
    print("OK button is clicked")

def processCancel():
    print(" cancel button is clicked")

window=Tk()#create a window 
btOK= Button(window,text="OK" ,fg="red",command=processOK)
btCancel=Button(window,text="Cancel",bg="yellow",command=processCancel)
btOK.pack()#place the OK button in the window
btCancel.pack()#place the cancel button in the window

window.mainloop()#create an event loop 


