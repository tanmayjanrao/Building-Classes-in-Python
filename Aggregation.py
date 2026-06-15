# Aggregation is a concept in which an object of one class can own or access another independent object of another class. 

## It represents Has-A’s relationship.
# It is a unidirectional association i.e. a one-way relationship. For example, a department can have students but vice versa is not possible and thus unidirectional in nature.
# In Aggregation, both the entries can survive individually which means ending one entity will not affect the other entity.



class Player:
    def __init__(self, name):
        self.name = name

class Team:
    def __init__(self):
        self.players = []  


p1 = Player("Kohli")
p2 = Player("Dhoni")


team = Team()
team.players = [p1, p2]  


del team
print(p1.name) 
print(p2.name)  