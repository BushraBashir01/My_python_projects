"""
Project: Tkinter Dynamic Bouncing Ball Physics Simulation
Purpose: Sumilates real_time physical movement and collision detection as objects bounce off window boundaries.
Key Concept: Boundary Collision Detection, Position Vector Updating, Canvas Shape Manipulation, Real_Time Physics Logic.
Usage: Showhow game physics fundamentals and real_time graphic state management in python.
"""
from tkinter import*
from random import randint

def getRandomColor():
    color="#"
    for j in range(6):
        color+=toHexChar(randint(0,15))
    return color

def toHexChar(hexvalue):
    if 0 <= hexvalue<=9:
        return chr(hexvalue+ord("0"))
    else:
        return chr(hexvalue-10+ord("A"))
    
class Ball:
    def __init__(self):
        self.x=0
        self.y=0
        self.dx=2
        self.dy=2
        self.radius=3
        self.color= getRandomColor()

class BounceBalls:
    def __init__(self):
        self.ballList=[]

        window=Tk()
        window.title("Bouncing Balls")

        self.width=360
        self.height=160
        self.canvas=Canvas(window,bg="white",width=self.width,height=self.height)

        self.canvas.pack()

        frame=Frame(window)
        frame.pack()
        btStop=Button(frame,text="stop",command=self.stop)
        btStop.pack(side=LEFT)
        btResume=Button(frame,text="Resume",command=self.resume)
        btResume.pack(side=LEFT)
        btAdd=Button(frame,text="Add",command=self.add)
        btAdd.pack(side=LEFT)
        btRemove=Button(frame,text="Remove",command=self.remove)
        btRemove.pack(side=LEFT)

        self.SleepTime=100
        self.isStopped=False
        self.animate()

    def stop(self):
            self.isStoped=True

    def resume(self):
            self.isStopped=False
            self.animate()

    def add(self):
            self.ballList.append(Ball())

    def remove(self):
            self.ballList.pop()

    def animate(self):
            while not self.isStopped:
                self.canvas.after(self.SleepTime)
                self.canvas.update()
                self.canvas.delete("ball")

                for ball in self.ballList:
                    self.redisplayBall(ball)

    def redisplayBall(self,ball):
            if ball.x>self.width or ball.x<0:
                ball.dx= -ball.dx

            if ball.y>self.height or ball.y<0:
                ball.dy= -ball.dy

            ball.x+=ball.dx
            ball.y+=ball.dy
            self.canvas.create_oval(ball.x-ball.radius,ball.y-ball.radius,
                                    ball.x+ball.radius,ball.y+ball.radius,fill=ball.color,tags="ball")

BounceBalls()
