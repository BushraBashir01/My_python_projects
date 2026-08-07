"""
Project:Tkinter Name Entry GUI Form 
Purpose:Demonstrates Creating an interactive desktop form to capture user input Python Tkinter library.
Key Concepts: Tkinter Widgets (Label,Entry,Button),Grid Layout Manger ,and Event Handling. 
usage:Serves as a foundational component for desktop application that form handling and data collection.
"""

from tkinter import *

window=Tk()
name_Label=Label(window,text="Name")
name_Label.grid(column=0,row=0)

txt=Entry(window,width=20) 
txt.grid(column=1,row=0)

name_Label=Label(window, text="City")
name_Label.grid(column=0,row=1)

txt=Entry(window,width=20)
txt.grid(column=1,row=1)

name_Label=Label(window,text="age")
name_Label.grid(column=0,row=2)

txt=Entry(window,width=20) 
txt.grid(column=1,row=2)

btn=Button(window,text="click me")
btn.grid(column=1,row=3)

window.mainloop()