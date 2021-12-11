rooms = []
class Room():
    def __init__(self, name, description, exit_message, short_desc, **kwargs):
        self.name = name
        self.exit_message = exit_message
        self.description = description
        self.short_desc = short_desc
        for key, value in kwargs.items():
            setattr(self, key, value)
        rooms.append(self)
        
        
def search_room(name):
    for room in rooms:
        if room.name == name:
            return room
    return None