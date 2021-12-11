from modules.item import *
from modules.enemy import *
from player import global_player as player1
class Weapon(Item):
    def __init__(self, name, description, value, weight, damage, type, cost, equip_message, unequip_message):
        self.damage = damage
        self.type = type
        self.cost = cost
        super().__init__(name, description, value, weight, equip_message, unequip_message)
    def use(self, target):
        player1.stamina-=self.stamina
        for i in player1.location.enemies:
            if i.name == target:
                i.health -= self.damage
                print("You hit the {} for {} damage!".format(i.name, self.damage))
                break