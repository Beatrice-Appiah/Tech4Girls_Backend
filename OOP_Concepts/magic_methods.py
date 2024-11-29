#!/bin/bash
# this script is to demontrate magic methods and property decorators

# The class Rectangle created
class Rectangle:
# Initializing the instance variables
    def __init__(self,length,width):
        self.length = length
        self.width = width
    
# Property method Area
    @property
    def area(self):
            return self.length * self.width
    
    # Property method Perimter
    @property
    def perimeter(self):
        return 2 * (self.length + self.width)
    
    # A dunder(magic) method __str__()
    def __str__(self):
         return f"\nRectangle(Length: {self.length}, Width: {self.width})"
    
    """ A dunder(magic) method __eq__() to compare 2 rectangles and check if their 
    area are equal. """
    def __eq__(self, other):
            return self.area == other.area 


# Instances for class Rectangle
rec1 = Rectangle(3, 6)
rec2 = Rectangle(4, 9)

# Printing out results for intsances using methods; Area
print(rec1.area)
print(rec2.area)

# Printing out results for intsances using methods; Perimeter
print(rec1.perimeter)
print(rec2.perimeter)

# Printing out results for instances using methods; __str__
print(rec1)
print(rec2)

# Printing out results for intsances using methods; __eq__
print(rec1 == rec2)