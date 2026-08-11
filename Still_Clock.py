"""
Project:Still Clock Widget (Tkinter GUI)
Purpose:A custom Tkinter Canvas widget to render a static analog clock face with customizable hoour,minute, and second hands.
Key Concept:Object-Oriented Programming (OOP), Tkinter Canvas Graphics, Mathematical Trigonometric Positioning(Sin/Cos).
Usage:Import StillClock, instanttiate it within a Tkinter window, and use setHour(), setMinute(), or setSecond() to update the display time.
"""

from tkinter import*
import math 
import time 

class StillClock(Canvas):
    def __init__(self, container,width=200,heiht=200):
        super().__init__(container,width=width,height=heiht,bg="white")
        self.__hour=0
        self.__minute=0
        self.__second=0
        self.drawClock()

    def getHour(self):return self.__hour
    def getMinute(self):return self.__minute
    def getSecond(self):return self.__second

    def setHour(self,Hour):
        self.__hour=Hour
        self.drawClock()

    def setMinute(self,minute):
        self.__minute= minute
        self.drawClock()

    def setSecond(self,second):
        self.__second=second
        self.drawClock()

    def drawClock(self):
        self.delete("all")

        radius=min(int(self["width"]),int(self["height"])) / 2-20
        xCenter=int(self["width"]) /2 
        yCenter=int(self["height"]) /2
        self.create_oval(xCenter-radius,yCenter-radius,xCenter+radius,yCenter+radius)

        self.create_text(xCenter,yCenter-radius+10,text="12")
        self.create_text(xCenter+radius-10,yCenter,text="3")
        self.create_text(xCenter,yCenter+radius-10,text="6")
        self.create_text(xCenter-radius+10,yCenter,text="9")

        sLenght=radius*0.8
        xSecond=xCenter+sLenght*math.sin(self.__second*(2*math.pi/60))
        ysecond=yCenter-sLenght*math.cos(self.__second*(2*math.pi/60))
        self.create_line(xCenter,yCenter,xSecond,ysecond,fill="red")

        mLenght=radius*0.65
        xMinute=xCenter+mLenght*math.sin(self.__minute*(2*math.pi/60))
        yMinute=yCenter-mLenght*math.cos(self.__minute*(2*math.pi/60))
        self.create_line(xCenter,yCenter,xMinute,yMinute,fill="blue",width=2)

        hLenght=radius*0.5
        xHour=xCenter+hLenght*math.sin((self.__hour%12+self.__minute/60)*(2* math.pi/12))
        yHour=yCenter-hLenght*math.cos((self.__hour%12+self.__minute/60)*(2*math.pi/12))
        self.create_line(xCenter,yCenter,xHour,yHour,fill="black",width=3)