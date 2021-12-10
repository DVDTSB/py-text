from world import global_world
from modules.room import search_room
coords = (0, 0)
def get_world(name):
    with open('resources/{}'.format(name), 'r') as f:
        rows = f.readlines()
    x_max = len(rows[0].split('\t'))
    for y in range(len(rows)):
        cols = rows[y].split('\t')
        for x in range(x_max):
            tile_name = cols[x].replace('\n', '')
            if tile_name == 'starting_room':
                coords = (x, y)
            global_world[(x, y)] = None if tile_name == '' else search_room(tile_name)
            
def get_room(x, y):
    if (x, y) in global_world:
        return global_world[(x, y)]
    else:
        return None
    
def print_exits(x, y):
    result = ""
    if get_room(x+1, y) is not None:
        result += "In the east you can see {}\n".format(get_room(x+1, y).short_desc)
    if get_room(x-1, y) is not None:
        result += "In the west you can see {}\n".format(get_room(x-1, y).short_desc)
    if get_room(x, y+1) is not None:
        result += "In the south you can see {}\n".format(get_room(x, y+1).short_desc)
    if get_room(x, y-1) is not None:
        result += "In the north you can see {}\n".format(get_room(x, y+1).short_desc)
    if result == "":
        result = "There are no exits from here."
    return result