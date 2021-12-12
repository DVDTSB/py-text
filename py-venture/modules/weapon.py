from modules.item import *
from modules.enemy import *
class Weapon(Item):
    def __init__(self, name, description, value, weight, damage, type, cost, equip_message, unequip_message):
        self.damage = damage
        self.type = type
        self.cost = cost
        super().__init__(name, description, value, weight, equip_message, unequip_message)