"""
Project:Interactive Mouse Click Event Handling 
Purpose:Captures dynamic user mouse inputs (click position and coordinates) directly on a window canvas.
Key Concept:Event_Driven Architecture, Event Binding('<Button-1>'),Coordinate Tracking, Dynamic Callbacks.
Usage:Demonstrates user_interaction handling essential for graphics applications and custom GUI control.
"""
from tkinter import*

class MouseKeyEventDemo:
    def __init__(self):
        window=Tk()
        window.title("EventDemo")
        canvas=Canvas(window,bg="white",width=200,height=100)
        canvas.pack()

        canvas.bind("<Button-1>",self.processMouseEvent)
        canvas.bind("<Key>",self.processKeyEvent)
        canvas.focus_set()

        window.mainloop()

    def processMouseEvent(self,event):
            print("clicked at",event.x,event.y)
            print("position on screen",event.x_root,event.y_root)
            print("which Button is clicked",event.num)

    def processKeyEvent(self,event):
            print("Keysym>",event.keysym)
            print("char>",event.char)
            print("Keycode>",event.Keycode)

MouseKeyEventDemo()

