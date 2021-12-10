import modules.action as action
from player import global_player
inventory = action.Action("Inventory", "You look in your inventory.",["i", "in", "inventory"], global_player.print_inventory)
statistics = action.Action("Statistics", "You search your mind to see a few of your stats.", ["stats", "statistics"], global_player.print_stats)
equip = action.Action("Equip", "You equip an item.", ["equip", "e"], global_player.equip_item)
unequip = action.Action("Unequip", "You unequip an item.", ["unequip", "u"], global_player.unequip_item)