class Room():
    def __init__(self, name, description, exit_message, short_description, **kwargs):
        self.name = name
        self.exit_message = exit_message
        self.description = description
        self.short_description = short_description
        for key, value in kwargs.items():
            setattr(self, key, value)