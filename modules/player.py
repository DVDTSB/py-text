from modules.world import world
class Player():
    def __init__(self, name, inventory, max_inventory, gold, hp, sp, max_hp, max_sp, attack, defense, coords):
        self.name = name
        self.inventory = inventory
        self.max_inventory = max_inventory
        self.gold = gold
        self.hp = hp
        self.sp = sp
        self.max_hp = max_hp
        self.max_sp = max_sp
        self.attack = attack
        self.defense = defense
        self.coords = list(coords)
        self.location = world[self.coords[0]][self.coords[1]]
        if self.location == None:
            print("ERROR: Player's location is None.")
    def equip_item(self, item):
        for i in self.location.items:
            if i.name.lower() == item[0].lower():
                print(i.equip_message)
                self.location.items.remove(i)
                self.inventory.append(i)
                return True
        print("There is no " + item[0] + " here.")
    def unequip_item(self, item):
        for i in self.inventory:
            if i.name.lower() == item[0].lower():
                print(i.unequip_message)
                self.location.items.append(i)
                self.inventory.remove(i)
                return True
        print("You don't have that item equipped.")