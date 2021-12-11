



from premade.rooms import *

def load():
    import modules.world as world
    world.get_world("map.txt")
    
    import modules.player as player
    import modules.item as item
    import modules.weapon as weapon
    import modules.armour as armour
    import modules.action as action
    
    #from player import global_player as player1
    #player.coords = world.coords
    #player1.inventory = [basic_sword, skull, chainmail_armour]