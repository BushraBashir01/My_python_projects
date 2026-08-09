"""
Project:Test Circle and Rectangle Inheritance
Purpose:Driver script to test and demonstrate Circle and Rectangle subclass derived from GeometricObject.
Key Concept:Object Instantiation ,Polymorphism,Driver Script Pattern.
Usage:Runs the main function to display properties and calculations for test shape instances.
"""

from Image.circle_from_Geometric import Circle 
from Image.rectangle_from_Geometric import Rectangle

def main():
    circle=Circle(2.5)
    print("A circle:",circle)
    print("the radius is",circle.getRadius())
    print("the area is",circle.getArea())
    print("the diameter is",circle.getDiameter())

    rectangle=Rectangle(2,4)
    print("\nk rectangle",Rectangle)
    print("the area is",Rectangle.getArea())
    print("the diameteris",Rectangle.getDiameter())

    main()
    

