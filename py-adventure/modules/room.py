rooms = []
class Room():
    def __init__(self, name, description, exit_message, short_desc, items, enemies):
        self.name = name
        self.exit_message = exit_message
        self.description = description
        self.short_desc = short_desc
        self.items = items
        self.enemies = enemies
        rooms.append(self)
    def print_room(self):
        print(self.description)
        if self.items != []:
            print("You see:")
            for item in self.items:
                print("a " + item.name.lower()+ ", ")
        
        
def search_room(name):
    for room in rooms:
        if room.name == name:
            return room
    return None