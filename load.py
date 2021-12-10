import modules.player as player
import modules.item as item
import modules.weapon as weapon
import modules.armour as armour
import modules.action as action
import modules.world as world

from premade.items import *
from premade.weapons import *
from premade.armours import *
from premade.actions import *

from player import global_player as player1

def load():
    world.get_world("map.txt")
    player.coords = world.coords
    player1.inventory = [basic_sword, skull, chainmail_armour]