from modules.world import get_room, startcoords, print_exits
from modules.room import *
from world import global_world 
class Player():
    def __init__(self, name, inventory, max_inventory_size, health, max_health, stamina, max_stamina, mana, max_mana, level, exp, next_level_multiplier, attack, defense, gold):
        self.name = name
        self.inventory = inventory
        self.max_inventory_size = max_inventory_size
        self.health = health
        self.max_health = max_health
        self.stamina = stamina
        self.max_stamina = max_stamina
        self.mana = mana
        self.max_mana = max_mana
        self.level = level
        self.exp = exp
        self.next_level_multiplier = next_level_multiplier
        self.attack = attack
        self.defense = defense
        self.gold = gold
        self.coords = list(startcoords)
        self.location = get_room(self.coords[0], self.coords[1])
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
        if len(self.inventory) == 0:
            print("You have nothing.")
        else:
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
        
    def go(self, a):
        direction = a[0]
        if direction.lower() == "north" or direction.lower() == "n":
            self.move_north()
        elif direction.lower() == "south" or direction.lower() == "s":
            self.move_south()
        elif direction.lower() == "east" or direction.lower() == "e":
            self.move_east()
        elif direction.lower() == "west" or direction.lower() == "w":
            self.move_west()
    
    def move(self, dx, dy):
        if get_room(self.coords[0]+dx, self.coords[1]+dy) != None:
            print(self.location.exit_message)
            self.coords[0] += dx
            self.coords[1] += dy
            self.location = get_room(self.coords[0], self.coords[1])
            self.location.print_room()
            print_exits(self.coords[0], self.coords[1])
        else:
            print("You can't go that way.")
    def move_north(self):
        self.move(0, -1)
    def move_south(self):
        self.move(0, 1)
    def move_east(self):
        self.move(1, 0)
    def move_west(self):
        self.move(-1, 0)    