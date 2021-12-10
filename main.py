import modules.player as player
import modules.item as item
import modules.weapon as weapon
import modules.armour as armour
import modules.action as action

from premade.items import *
from premade.weapons import *
from premade.armours import *
from premade.actions import *

from player import global_player as player1

from load import load

load()

while(True):
    command = input("What do you want to do? ")
    action.execute_action(command)