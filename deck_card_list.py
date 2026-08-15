"""
Project:Deck of Cards Simulation
Purpose:Models a standard deck of playing cards using object_oriented principles, including card image, Shuffling, and dealing logic
Key Concept:Class structures, Data Abstraction, List Manipulation, Randomization Algoritmss.
Usage:Serve as a modular foundation for card_base games and probability simulations in python.
"""
from tkinter import*
import random

class DeckofCardsGUI:
    def __init__(self):
        window=Tk()
        window.title("pick four Cards Randomly")

        self.ImageList=[]
        for i in range(2,10):
            self.ImageList.append(PhotoImage(file="Image/card/str"+ str(i)+ ".png"))

        frame=Frame(window)
        frame.pack()


        self.labellist=[]
        for i in range(4):
            label=Label(frame,image=self.ImageList[i])
            label.pack(side=LEFT)
            self.labellist.append(label)

        Button(window,text="shuffle",command=self.shuffle).pack()

        window.mainloop()

    def shuffle(self):
            random.shuffle(self.ImageList)
            for i in range(4):
                self.labellist[i]["image"]=self.ImageList[i]

DeckofCardsGUI()
