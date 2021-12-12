def load():
    import modules.world as world
    import resources.rooms
    world.get_world("map.txt")
    
    print(world.startcoords)
    
    import resources.player as player
    player.global_player.location.print_room()
    world.print_exits(player.global_player.coords[0], player.global_player.coords[1])