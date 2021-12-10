
from modules.action import Action
from player import global_player
inventory = Action("Inventory", "You look in your inventory.",["i", "in", "inventory"], global_player.print_inventory)
statistics = Action("Statistics", "You search your mind to see a few of your stats.", ["stats", "statistics"], global_player.print_stats)
equip = Action("Equip", "You equip an item.", ["equip", "e"], global_player.equip_item)