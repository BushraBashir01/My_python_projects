"""
Project:Circle Subclass inheriting Geometric Object 
Purpose:Implements a Circle shape class derived from the parent GeometricObject class with radius-specific calculations.
Key Concept:OOP Inheritance,Method  Overriding, Encapsulation,and Geometric Area/Perimeter Formulas.
Usage:Provides functionality to create circle instances with specialized area and perimeter computation.
"""

from Image.geometrics_objects import GeometricObject
import math 

class Circle(GeometricObject):
    def __init__(self, radius,color="green",filled=True):
        super().__init__(color,filled)
        self.__radius=radius

    def getRadius(self):
        return self.__radius

    def setRadius(self,radius):
        self.__radius=radius

    def getArea(self):
        return self.__radius*self.__radius*math.pi

    def getDiameter(self):
        return 2 *self.__radius

    def getPerimeter(self):
        return 2 *self.__radius*math.pi

    def printCircle(self):
        print(self.__str__()+"radius:"+str(self.__radius))

my_Circle= Circle(7,"yellow",True)

my_Circle.printCircle()

print("circle Area:",my_Circle.getArea())
print("circle Diameter:",my_Circle.getDiameter())

