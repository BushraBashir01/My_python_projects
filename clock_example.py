"""
Project:Interactive Clock Controller (Tkinter GUI)
Purpose:To build a user interface that allows users to manually set and update the analog clock time using input entry fields.
Key Concept:Custom Widget Integration(StillClock),Tkinter Control Variables(IntVar),Event Handling with Buttons,UI Layout Management.
Usage:Run the script to open the main window, enter value for Hour, Minute, and Second, then clock"Set New Time" to update the clock display.
"""
from tkinter import *
from Image.Still_Clock import StillClock

class displayClock:
    def __init__(self):
        window=Tk()
        window.title("Change Clock Time")

        self.clock=StillClock(window)
        self.clock.pack()

        frame=Frame(window)
        frame.pack()
        Label(frame,text="Hour:").pack(side=LEFT)
        self.hour=IntVar()
        self.hour.set(self.clock.getHour())
        Entry(frame,textvariable=self.hour,width=4).pack(side=LEFT)
        Label(frame,text="Minute:").pack(side=LEFT)
        self.minute=IntVar()
        self.minute.set(self.clock.getMinute())
        Entry(frame,textvariable=self.minute,width=4).pack(side=LEFT)
        Label(frame,text="Second:").pack(side=LEFT)
        self.second=IntVar()
        self.second.set(self.clock.getSecond())
        Entry(frame,textvariable=self.second,width=4).pack(side=LEFT)
        Button(frame,text="Set New Time",command=self.SetNewTime).pack(side=LEFT)
        window.mainloop()

    def SetNewTime(self):
        self.clock.setHour(self.hour.get())
        self.clock.setMinute(self.minute.get())
        self.clock.setSecond(self.second.get())

displayClock()
