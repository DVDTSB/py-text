from modules.item import Item
class Food(Item):
    def __init__(self, name, description, value, weight, health, stamina, mana, equip_message, unequip_message, eat_message):
        self.name = name
        self.description = description
        self.value = value
        self.weight = weight
        self.health = health
        self.stamina = stamina
        self.mana = mana
        self.equip_message = equip_message
        self.unequip_message = unequip_message
        self.eat_message = eat_message
