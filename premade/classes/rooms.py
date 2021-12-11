from modules.room import *
class LootRoom(Room):
    def __init__(self, name, description, exit_message, short_desc, loot):
        self.loot = loot
        super.__init__(name, description, exit_message, short_desc)
        rooms.append(self)

