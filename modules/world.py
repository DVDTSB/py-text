
from modules.room import search_room

def get_world(name):
    world = [[None for x in range(10)] for y in range(10)] 
    with open("resources/{}".format(name), "r") as f:
        rows = f.readlines()
    x_max = len(rows[0].split("\t"))
    for y in range(len(rows)):
        cols = rows[y].split("\t")
        for x in range(x_max):
            tile_name = cols[x].replace("\n","")
            if tile_name != "" and search_room(tile_name)!=None:
                world[x][y] = search_room(tile_name)
    return world

world = get_world("world.txt")