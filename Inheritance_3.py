class Animal :
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def intro (self):
        return f"Welcome {self.name} ! "


class Dog(Animal):
    def __init__(self,name,age,breed):
        super().__init__(name,age)
        self.breed=breed

    def make_sound(self):
        return "Woof!"

    def __str__(self):
        return f"The name of the dog is {self.name} age is {self.age} breed is {self.breed}"

obj2=Dog("Tom",18,"Great Dane")
obj = Animal("Tom", 10)
print(obj.intro())
print(obj2)