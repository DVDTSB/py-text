from modules.room import Room
from premade.objects.rooms import *
import items as items

starting_room = room.Room(
    "Starting room",
    "You find yourself in a dark room, the only light coming from a torch. It looks empty.", 
    "You leave the dark room and head to the next deistanation.", 
    "the dark room you have started your journey in.",
    [items.skull],[]
)
path_room = room.Room(
    "Path",
    "An empty path, leading to another room",
    "You continue on your jorney",
    "a path.",
    [],[]
)