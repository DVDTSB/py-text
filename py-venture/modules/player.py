from modules.world import get_room, startcoords, print_exits
from modules.room import *
from modules.food import Food


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

    def print_inventory(self):
        if len(self.inventory) == 0:
            print("You have nothing.")
        else:
            print("Inventory:")
            for item in self.inventory:
                print(item.name + " : " + item.description +
                      " The value of this item is " + str(item.value) + " gold.")

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

    def eat(self, food):
        for i in self.inventory:
            if i.name.lower() == food[0].lower():
                if type(i) == Food:
                    print("You eat the " + i.name + ".")
                    print(i.eat_message)
                    self.health += i.health
                    self.stamina += i.stamina
                    self.mana += i.mana
                    if self.health > i.max_health:
                        self.health = i.max_health
                    if self.mana > i.max_mana:
                        self.mana = i.max_mana
                    if self.stamina > i.max_stamina:
                        self.stamina = i.max_stamina
                    self.inventory.remove(i)
                    return True

    def move_north(self):
        self.move(0, -1)

    def move_south(self):
        self.move(0, 1)

    def move_east(self):
        self.move(1, 0)

    def move_west(self):
        self.move(-1, 0)
