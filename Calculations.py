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


a = Calculation(8)
b = Calculation(35)
percentage = a.percentage(b.num)

print(a + b)        
print(a - b)        
print(a * b)        
print(a / b)       
print(a.square())  
print(percentage) 

