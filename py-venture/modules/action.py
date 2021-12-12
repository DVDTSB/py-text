actions = []
class Action():
    def __init__(self, name, description, keywords, function):
        self.name = name
        self.description = description
        self.keywords = keywords
        self.function = function
        
        actions.append(self)
    def execute(self, *argv):
        if argv[0]:
            self.function(argv)
            return True
        self.function()
        

def execute_action(command):
    for ac in actions:
        for keyword in ac.keywords:
            if (command.lower().split()[0]==keyword):
                ac.execute("".join(command.split(" ", 1)[1]))
                return True
    print("I don't understand")