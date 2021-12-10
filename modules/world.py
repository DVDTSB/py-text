from world import global_world
def get_world(name):
    with open('resources/{}'.format(name), 'r') as f:
        rows = f.readlines()
    x_max = len(rows[0].split('\t'))
    for y in range(len(rows)):
        cols = rows[y].split('\t')
        for x in range(x_max):
            tile_name = cols[x].replace('\n', '')
            if tile_name == 'StartingRoom':
                global starting_position
                starting_position = (x, y)
            global_world[(x, y)] = None if tile_name == '' else getattr(__import__('tiles'), tile_name)(x, y)
            
def get_room(x, y):
    if (x, y) in global_world:
        return global_world[(x, y)]
    else:
        return None