import modules.room as room
import premade.objects.items as items
import premade.objects.food as food
starting_room = room.Room(
    "Starting room",
    "You find yourself in a dark room, the only light coming from a torch. It looks empty.", 
    "You leave the dark room and head to the next deistanation.", 
    "the dark room you have started your journey in.",
    [items.skull],[]
)
second_room = room.Room(
    "Second room",
    "A spacios room, with enscriptions on the walls and floor. A weird shine comes from them.", 
    "You leave the room, the light coming from the runes is getting dimmer", 
    "a room with shining runes.",
    [food.carrot],[]
)
path_room = room.Room(
    "Path",
    "An empty path, leading to another room",
    "You continue on your jorney",
    "a path.",
    [],[]
)
bananier_room = room.Room(
    "Bananier room", 
    "A room with a bananier", 
    "You leave the room", 
    "a room with a bananier",
    [],[]
)