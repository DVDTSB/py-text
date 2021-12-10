from modules.item import *
class Weapon(Item):
    def __init__(self, name, description, value, weight, damage, type, equip_message, unequip_message):
        self.damage = damage
        self.type = type
        super().__init__(name, description, value, weight, equip_message, unequip_message)