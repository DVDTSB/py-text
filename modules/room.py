rooms = []
class Room():
    def __init__(self, name, description, exit_message, short_desc, items, enemies, npcs):
        self.name = name
        self.description = name
        self.exit_message = exit_message
        self.short_desc = short_desc
        self.items = items
        self.enemies = enemies
        self.npcs = npcs
        rooms.append(self)
    def print_room(self):
        print(self.description)
        if(self.items):
            print("Items:")
            for item in self.items:
                print("\t" + item.description)
        if(self.enemies):
            print("Enemies:")
            for enemy in self.enemies:
                print("\t" + enemy.description)
        if(self.npcs):
            print("NPCs:")
            for npc in self.npcs:
                print("\t" + npc.description)
                
def search_room(name):
    for room in rooms:
        if(room.name == name):
            return room
    return None

room1 = Room("Room1", "This is room 1", "You exit the room", "Room 1", [], [], [])