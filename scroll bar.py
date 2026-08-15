"""
Project:Tkinter Scrollbar Component 
Purpose:Demonstrates adding scrollbar functionally to overflow Tkinter widgets like Listbox and Canvas.
Key Concept:widget Linking, Dynamic Y_scroll Management ,Event Binding,UI Navigation.
Usage:Serves as a reusable component pattern for managing large visual datasets in desktop interfaces.
"""
from tkinter import*

class ScrollText:
    def __init__(self):
        window=Tk()
        window.title("ScrollTextDemo")

        frame1=Frame(window)
        frame1.pack()
        scrollbar=Scrollbar(frame1)
        scrollbar.pack(side=RIGHT,fill=Y)
        text=Text(frame1,width=80,height=20,wrap=WORD,yscrollcommand=scrollbar.set)
        text.pack()
        scrollbar.config(command=text.yview)

        window.mainloop()

ScrollText()
