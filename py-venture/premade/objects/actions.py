
from modules.action import Action
from player import global_player
inventory = Action("Inventory", "You look in your inventory.",["i", "in", "inventory"], global_player.print_inventory)
statistics = Action("Statistics", "You search your mind to see a few of your stats.", ["stats", "statistics"], global_player.print_stats)
equip = Action("Equip", "You equip an item.", ["equip", "e"], global_player.equip_item)
unequip = Action("Unequip", "You unequip an item.", ["unequip", "u"], global_player.unequip_item)
go = Action("Go", "You go somewhere.", ["go", "g"], global_player.go)