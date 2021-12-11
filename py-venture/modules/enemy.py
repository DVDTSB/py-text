from modules.item import *
class Enemy():
    def __init__(self, name, keywords, inventory, health, max_health, stamina, max_stamina, drop_exp, attack, defense, gold, location):
        self.name = name
        self.inventory = inventory
        self.health = health
        self.max_health = max_health
        self.stamina = stamina
        self.max_stamina = max_stamina
        self.drop_exp = drop_exp
        self.attack = attack
        self.defense = defense
        self.gold = gold
        self.location = location
        self.is_alive = True
        self.keywords = keywords
    def add_health(self, amount):
        self.health += amount
    def add_attack(self, amount):
        self.attack += amount
    def add_defense(self, amount):
        self.defense += amount
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
    