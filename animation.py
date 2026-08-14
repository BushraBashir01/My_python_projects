"""
Project: Tkinter Canvas Basic GUI Animation
Purpose: Demonstrates frame_by_frame graphic animation using Tkinter Canvas and scheduled visual updates.
Key Concept: Tkinter Canvas Widget, Coordinate Space Movement, Frame Refreshing Logic, Visual Rendering.
Usage: Serves as a foundational blueprint for rendering continuous graphic motion in pyton desktop applications.
"""
from tkinter import*

class AnimationDemo:
    def __init__(self):
        window=Tk()
        window.title("AnimationDemo")

        width=260 # width of canvas
        self.canvas=Canvas(window,bg="white",width="250",height="150")
        self.canvas.pack()


        self.canvas.create_text(40,50,text="hello i am bushra",tags="text")
        ax=3
        x=40

        while True:
            self.canvas.move("text",ax,0)
            self.canvas.after(100)
            self.canvas.update()
            x+= ax

            if x< width:
                pass
            else:
                x=0
                self.canvas.delete("text")

                self.canvas.create_text(x,30,text="hello i am bushra",tags="text")

        window.mainloop()

AnimationDemo()







