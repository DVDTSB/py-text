from load import load

load()

import modules.action as action
from premade.objects.actions import *

while(True):
    command = input("What do you want to do? ")
    action.execute_action(command)