"""
Project:Tkinter Mini Calculator Application
Purpose:Implements a functional desktop calculator performing standard arithmetic operations througth an interactive GUI layout.
Key Concept:Tkinter Layout Grid, Event_Driven Callbacks, Expression Evaluation,State Handling.
Usage:Demonstrates real_time mathematical expression processing and desktop utility UI design.
"""
from tkinter import *

class MenuDemo:
    def __init__(self):
        window=Tk()
        window.title=("MenuDemo")

        #create a menubar
        menubar= Menu(window)
        window.config(menu=menubar) #display a menubar

        operationmenu=Menu(menubar,tearoff=0)
        menubar.add_cascade(label="operation",menu=operationmenu)
        operationmenu.add_command(label="Add",command=self.add)
        operationmenu.add_command(label="Subtract",command=self.subtract)
        operationmenu.add_separator()
        operationmenu.add_command(label="Multiply",command=self.multiply)
        operationmenu.add_command(label="Divide",command=self.divide)

        exitmenu=Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Exit",menu=exitmenu)
        exitmenu.add_command(label="Quit",command=window.quit)

        frame0=Frame(window)
        frame0.grid(row=1,column=1,sticky=W)

        plusImage=PhotoImage(file="Image/plus.png")
        minusImage=PhotoImage(file="Image/minus.png")
        timesImage=PhotoImage(file="Image/times.png")
        divideImage=PhotoImage(file="Image/divide.png")

        Button(frame0,image=plusImage,command=self.add).grid(row=1,column=1,sticky=W)
        Button(frame0,image=minusImage,command=self.subtract).grid(row=1,column=2)
        Button(frame0,image=timesImage,command=self.multiply).grid(row=1,column=3)
        Button(frame0,image=divideImage,command=self.divide).grid(row=1,column=4)

        frame1=Frame(window)
        frame1.grid(row=2,column=1,pady=10)
        Label(frame1,text="number 1:").pack(side=LEFT)
        self.v1=StringVar()
        Entry(frame1,width=5,textvariable=self.v1,justify=RIGHT).pack(side=LEFT)
        Label(frame1,text="number2:").pack(side=LEFT)
        self.v2=StringVar()
        Entry(frame1,width=5,textvariable=self.v2,justify=RIGHT).pack(side=LEFT)
        Label(frame1,text="Result:").pack(side=LEFT)
        self.v3=StringVar()
        Entry(frame1,width=5,textvariable=self.v3,justify=RIGHT).pack(side=LEFT)


        frame2=Frame(window)
        Button(frame2,text="Add",command=self.add).pack(side=LEFT)
        Button(frame2,text="subtract",command=self.subtract).pack(side=LEFT)
        Button(frame2,text="multiply",command=self.multiply).pack(side=LEFT)
        Button(frame2,text="divide",command=self.divide).pack(side=LEFT)

        window.mainloop()

    def add(self):
        self.v3.set(eval(self.v1.get())+eval(self.v2.get()))
    def subtract(self):
        self.v3.set(eval(self.v1.get())-eval(self.v2.get()))
    def multiply(self):
        self.v3.set(eval(self.v1.get())*eval(self.v2.get()))
    def divide(self):
        self.v3.set(eval(self.v1.get())/eval(self.v2.get()))

MenuDemo()



    