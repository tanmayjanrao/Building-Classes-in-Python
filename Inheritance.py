class School:

    def __init__(self,school_name):
        self.school_name=school_name
        print("Parent constructor")

  

    def show(self):
        return self.school_name

class Student(School):

    def __init__(self, name,rank,school_name):
        print("inside child class")
        super().__init__(school_name)
        self.name=name
        self.rank=rank
    
    def show(self):
        return self.school_name
    
    def __str__(self):  
        return f"My name is {self.name}, My rank is {self.rank}, My school is {self.school_name}"


obj=Student("TJ",1,"SRV")
print(obj)
print(obj.show())