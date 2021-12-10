from modules.item import *
class Player():
    def __init__(self, name, inventory, max_inventory_size, health, max_health, stamina, max_stamina, level, exp, next_level_multiplier, attack, defense, gold, starting_location):
        self.name = name
        self.inventory = inventory
        self.max_inventory_size = max_inventory_size
        self.health = health
        self.max_health = max_health
        self.stamina = stamina
        self.max_stamina = max_stamina
        self.level = level
        self.exp = exp
        self.next_level_multiplier = next_level_multiplier
        self.attack = attack
        self.defense = defense
        self.gold = gold
        self.starting_location = starting_location
        self.is_alive = True
    def add_gold(self, amount):
        self.gold += amount
    def add_exp(self, amount):
        self.exp += amount
    def equip_item(self, item):
        print(item.equip_message)
        self.inventory.append(item)
    def unequip_item(self, item):
        for i in self.inventory:
            if i.name.lower() == item[0].lower():
                print(i.unequip_message)
                self.inventory.remove(i)
                return True
        print("You don't have that item equipped.")
    def add_health(self, amount):
        self.health += amount
    def add_attack(self, amount):
        self.attack += amount
    def add_defense(self, amount):
        self.defense += amount
    def add_level(self, amount):
        self.level += amount
    def set_location(self, location):
        self.location = location
    def print_inventory(self):
        print("Inventory:")
        for item in self.inventory:
            print(item.name + " : " + item.description + " The value of this item is " + str(item.value) + " gold.")
    def print_stats(self):
        print("Name: " + self.name)
        print("Level: " + str(self.level))
        print("Experience: " + str(self.exp))
        print("Health: " + str(self.health) + "/" + str(self.max_health))
        print("Stamina: " + str(self.stamina) + "/" + str(self.max_stamina))
        print("Attack: " + str(self.attack))
        print("Defense: " + str(self.defense))
        print("Gold: " + str(self.gold))
    