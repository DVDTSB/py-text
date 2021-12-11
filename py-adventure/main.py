from load import load

load()

import modules.action as action


from player import global_player as player1


while(True):
    command = input("What do you want to do? ")
    action.execute_action(command)