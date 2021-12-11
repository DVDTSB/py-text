from load import load

load()

import modules.player as player
import modules.item as item
import modules.weapon as weapon
import modules.armour as armour
import modules.action as action

from premade.objects.items import *
from premade.objects.weapons import *
from premade.objects.armours import *
from premade.objects.actions import *

from player import global_player as player1


while(True):
    command = input("What do you want to do? ")
    action.execute_action(command)