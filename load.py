from premade.objects.rooms import *
def load():
    import modules.world as world
    world.get_world("map.txt")
    starting_room.print_room()
    world.print_exits(world.startcoords[0],world.startcoords[1])