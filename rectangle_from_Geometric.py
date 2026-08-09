"""
Project:Rectangle Subclass inheriting GeomtricObject 
Purpose:Implements a Rectangle shape class derived from GeometricObject with width and height calculations.
Key Concept:OOP Inheritance,Encapsulation,Method Overriding, Geometric Formulas.
Usage:Creates rectangle instances to compute area and diameter.
"""
from Image.geometrics_objects import GeometricObject

class Rectangle(GeometricObject):
    def __init__(self,width,height,color="green",filled=True):
        super().__init__(color,filled)
        self.__width=width
        self.__height=height

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height

    def setHeight(self,height):
        self.__height=height

    def getArea(self):
        return self.__width*self.__height

    def getDiameter(self):
        return 2*(self.__width+self.__height)

    def printRectangle(self):
        print(self.__str__()+"width"+str(self.__width)+"height:"+str(self.__height))

my_Rectangle=Rectangle(11,8,"blue",True)

my_Rectangle.printRectangle()

print("rectangle Area:",my_Rectangle.getArea())
print("rectangle Diameter:",my_Rectangle.getDiameter())