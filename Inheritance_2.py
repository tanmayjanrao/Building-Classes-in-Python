class School:

    def __init__(self,school_name):
        self.school_name=school_name
        print("Parent constructor")

  

    def show(self):
        return self.school_name

class Student(School):

    
    def show(self):
        return self.school_name
    
    def __str__(self):  
        return f"My school is {self.school_name}"


obj=Student("SRV")
print(obj)
print(obj.show())