import random
from player import global_player as player1
class Spell():
    def __init__(self, name, description,  cost, type, function, effect_message):
        self.name = name
        self.description = description
        self.cost = cost
        self.type = type
        self.function = function
        self.effect_message = effect_message
    def cast(self):
        self.function()
        print(self.effect_message)
        player1.mana -= self.cost
