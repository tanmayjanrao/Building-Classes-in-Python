class School:

    def __init__(self, school_name):
        self.school_name = school_name
        print("Parent constructor")


    def show(self):
        return self.school_name


class Student(School):

    def __init__(self, school_name, name):
        super().__init__(school_name)
        self.name = name

    def show(self):
        return self.school_name

    def __str__(self):
        return f"My school is {self.school_name}"

    def intro(self):
        return f"My name is {self.name}."


obj = Student("SRV", "Tanmay")

print(obj)
print(obj.show())
print(obj.intro())
