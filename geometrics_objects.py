"""
Project: Geometric Object Base Class (OOP Architecture)
Purpose: Serves as the parent superclass definig comman geometric properties like color and filled status.
Key Concepts: Object-Oriented Programming (OOP),Encapsulation,Class Construction, and Getter/Setter Methods.
Usage: Acts as the base foundational blueprint for specific 2D shapes (Circle,Rectangle,etc..).
"""

class GeometricObject:
    def __init__(self,Color="green",filled=True):
        self.__color=Color
        self.__filled=filled

    def getColor(self):
        return self.__Color

    def setColor(self,color):
        self.__color=color

    def isfilled(self):
        return self.__filled

    def setfilled(self,filled):
        self.__filled=filled

    def __str__(self):
        return "color:"+ self.__color+ "and filled"+ str(self.__filled)
    
Shape=GeometricObject("red",False)
#print(Shape)
#Shape.SetColor("blue")
#Shape.setfilled(True)

#print("After modification ",Shape)



        