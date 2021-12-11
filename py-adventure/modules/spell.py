import random
from player import global_player as player1
class Spell():
    def __init__(self, name, cost, type, function):
        self.name = name
        self.cost = cost
        self.type = type
        self.function = function
    def cast(self):
        self.function()
        player1.mana -= self.cost
