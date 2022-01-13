class Item():
    def __init__(self, name, description, value, equip_message = "You equiped the{name}", unequip = "You unequiped the{name}"):
        self.name = name
        self.description = description
        self.value = value
        self.equip_message = equip_message
        self.unequip = unequip
        