import math
from math import sqrt

class Calculation:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return Calculation(self.num + other.num)

    def __sub__(self, other):
        return Calculation(self.num - other.num)

    def __mul__(self, other):
        return Calculation(self.num * other.num)

    def __truediv__(self, other):
        return Calculation(self.num / other.num)

    def square(self):
        return self.num ** 2

    def __str__(self):
        return str(self.num)  

    def percentage(self, total_marks):
        return (self.num / total_marks) * 100


class Circle:

    def __init__(self, radius):
        self.radius=radius
        
    def side (self):
        return f"The side of the Circle is {math.pi * self.radius **2}"

    def Diameter(self):
       return f"The Diameter of the circle is {2*self.radius}"  

    def side_of_a_Semicircle(self):
        return f"The side_of_a_Semicircle is {( math.pi * self.radius ** 2 ) / 2}"

    def Circumference(self):
        return f"The Circumference of the circle is { 2 * math.pi * self.radius}"
    
    def perimeter_of_circle(self):
        return f"The Perimeter of the circle is {math.pi * self.radius  + 2 * self.radius}"
                                                     
class Square:

    def __init__(self, side):
        self.side = side
        self.perimeter = 4 * side
        self.area = side ** 2
        self.diagonal = side * sqrt(2)

    def Area_of_square(self):
        return f"The Area of square is {self.area}"

    def Perimeter_of_a_Square(self):
        return f"The Perimeter of a Square is {self.perimeter}"

    def Side_Length_from_Perimeter(self):
        return f"The Side length from the perimeter is {self.perimeter / 4}"

    def Side_Length_from_Area(self):
        return f"The Side Length from the Area is {sqrt(self.area)}"

    def Diagonal_of_square(self):
        return f"The Diagonal of the Square is {self.diagonal}"

    def Side_Length_from_Diagonal(self):
        return f"The Side Length from the Diagonal is {self.diagonal / sqrt(2)}"

    def Area_from_Diagonal(self):
        return f"The Area from the Diagonal is {(self.diagonal ** 2) / 2}"

    def Diagonal_from_Area(self):
        return f"The Diagonal from the Area is {sqrt(2 * self.area)}"
    


### pick one square and derive everything from it
obj = Square(5)

print(obj.Area_of_square())
print(obj.Perimeter_of_a_Square())
print(obj.Side_Length_from_Perimeter())
print(obj.Side_Length_from_Area())
print(obj.Diagonal_of_square())
print(obj.Side_Length_from_Diagonal())
print(obj.Area_from_Diagonal())
print(obj.Diagonal_from_Area())

















                                                   
'''
A = Circle(18)
print(A.side())
print(A.Diameter())
print(A.side_of_a_Semicircle())
print(A.Circumference())
print(A.perimeter_of_circle())

a = Calculation(8)
b = Calculation(35)
percentage = a.percentage(b.num)

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a.square())
print(percentage)
'''