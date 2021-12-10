from modules.item import *
class Armour(Item):
    def __init__(self, name, description, value, weight, defense, type, equip_message, unequip_message):
        self.damage = defense
        self.type = type
        super().__init__(name, description, value, weight, equip_message, unequip_message)
    