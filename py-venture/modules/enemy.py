from modules.item import *
#from resources.player import global_player as player
import random
class Enemy():
    def __init__(self, name, description, keywords, attacks, health, max_health, stamina, max_stamina, drop_exp, attack, defense):
        self.name = name
        self.description = description
        self.keywords = keywords
        self.attacks = attacks
        self.health = health
        self.max_health = max_health
        self.stamina = stamina
        self.max_stamina = max_stamina
        self.drop_exp = drop_exp
        self.attack = attack
        self.defense = defense
        self.is_alive = True

    def print_stats(self):
        print("Name: " + self.name)
        print("Description: " + self.description)
        print("Health: " + str(self.health) + "/" + str(self.max_health))
        print("Stamina: " + str(self.stamina) + "/" + str(self.max_stamina))
        print("Attack: " + str(self.attack))
        print("Defense: " + str(self.defense))
        print("Gold: " + str(self.gold))
    """def attack_player(self):
        attack = self.attacks(random.randint(1, len(self.attacks) - 1))
        player.health -= int(attack.damage*(self.attack-10)/(self.defense-10))
        print("The " + self.name + " attacks you for " + str(int(attack.damage*(self.attack-10)/(self.defense-10))) + " damage!")
        """