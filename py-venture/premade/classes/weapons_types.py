import modules.weapon as weapon
class Meele(weapon.Weapon):
    def __init__(self, name, description, value, weight, damage, type, equip_message, unequip_message):
        self.damage = damage
        self.type = type
        super().__init__(name, description, value, weight, equip_message, unequip_message)

class Ranged(weapon.Weapon):
    def __init__(self, name, description, value, weight, damage, range, type, equip_message, unequip_message, *args):
        self.damage = damage
        self.type = type
        self.range = range
        super().__init__(name, description, value, weight, equip_message, unequip_message)


