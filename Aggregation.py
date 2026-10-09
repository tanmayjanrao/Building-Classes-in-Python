
# Aggregation is a concept in which an object of one class can own or access another independent object of another class.

# It represents Has-A's relationship
# It is a unidirectional association i.e. a one-way relationship. For example, a department can have students but vice versa is not possible and thus unidirectional in nature.
# In Aggregation, both the entities can survive individually, which means ending one entity will not affect the other entity.


class Player:
    def __init__(self, name):
        self.name = name

    def show_player(self):
        print("Player Name:", self.name)


class Team:
    def __init__(self):
        self.players = []

    # Adding an existing Player object to the Team
    def add_player(self, player):
        self.players.append(player)

    # Displaying all players belonging to the Team
    def show_players(self):
        for player in self.players:
            player.show_player()


p1 = Player("Kohli")
p2 = Player("Dhoni")

team = Team()
team.add_player(p1)
team.add_player(p2)

team.show_players()

del team  # Deleting the Team object

# Player objects still exist independently
print(p1.name)
print(p2.name)
