class Greet:

    def __init__(self, name, country):
        self.name = name
        self.country = country

    def greeting(self):
        if self.country == "india":
            print(f"Namaste {self.name}")
        else:
            print(f"Hello {self.name}")

def multiply(a,b):
    return (a*b)

a = Greet("tanmay", "india")
a.greeting()


# with print we only get the result but with return being used the returned value can be used again
m=multiply(8,8)
print(m)
m=m+10
print(m)