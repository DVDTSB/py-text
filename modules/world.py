from world import global_world
from modules.room import search_room
def get_world(name):
    for x in range(-6, 6):
        for y in range(-6, 6):
            global_world[(x, y)] = None
    with open('resources/{}'.format(name), 'r') as f:
        rows = f.readlines()
    x_max = len(rows[0].split('\t'))
    for y in range(len(rows)):
        cols = rows[y].split('\t')
        for x in range(x_max):
            tile_name = cols[x].replace('\n', '')
            
            if tile_name == 'Starting room':
                global startcoords 
                startcoords = (x, y)
                print("Starting room found at {}".format((x, y)))
            
            if tile_name == "":
                global_world[(x, y)].name = "banana"
            
            elif search_room(tile_name) != None:
                global_world[(x,y)]=search_room(tile_name)
                print(global_world[(x,y)].description)
            
def get_room(x, y):
    try:
        if global_world[(x,y)] != None:
            return global_world[(x, y)]
        return None
    except:
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