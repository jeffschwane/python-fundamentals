'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''
from math import pi

class Rectangle:
    """Models a rectangle constructed by length and width.
    
    ...

    Attributes
    ----------
    length : int
        length of the rectangle
    width : int
        width of the rectangle

    Methods
    -------
    area()
        Calculates the area of the rectangle.
    perimeter()
        Calculates the perimeter of the rectangle.
    """

    def __init__(self, length, width):
        self.length = length
        self. width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


class Circle:
    """Models a circle constructed by radius.
    
    ...

    Attributes
    ----------
    radius : int
        radius of the circle

    Methods
    -------
    area()
        Calculates the area of the circle.
    circumference()
        Calculates the circumference of the circle.
    """
    
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return pi * self.radius ** 2

    def circumference(self):
        return 2 * pi * self.radius

r = Rectangle(5,4)
c = Circle(5)
print(r.area())
print(r.perimeter())
print(c.area())
print(c.circumference())