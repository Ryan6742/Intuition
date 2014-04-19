class Player():
    def __init__(self, start_room):
        self.current_room = start_room
        self.items = {}
        self.health = 100
        self.facing = 0
    def add_item(self, item):
        self.items[item.name] = item
    def rm_item(self, item):
        return self.items.pop(item.name)
    def input(self):
        return raw_input(": ").lower()

class Event():
	def __init__(self, name):
		self.name = name
        

class Room():
    def __init__(self, description = "", objects = {}, events = {}, dark = False):
        self.description = description
        self.objects = objects
        self.events = events
        self.dark = dark
        self.conditional = ""
    def add_door(self, direction, door):
    	self.objects[direction] = door
    def add_item(self, item):
    	self.objcets[item.name] = item
    def rm_item(self, item):
        return self.objects.pop(item)
    def add_NPC(self, NPC):
    	self.objects[NPC.name] = NPC
    def add_event(self, event):
        self.events[event.name] = event

class Door():
    def __init__(self, room1, room2, description = "", locked = False):
        self.description = description
        self.conditional = ""
        connecting = [room1, room2]
        self.locked = locked
        description = ""
    def lock(self):
        self.locked = True
    def unlock(self):
        self.locked = False

class Item():
    def __init__(self, name, description = "", takable = False):
        self.name = name
        self.description = description
        self.conditional = ""
        self.takable = takable
        self.alt_names = []
    def use(self):
        return "It does nothing"

class NPC():
    def __init__(self, name, description = "", talkable = False):
        self.name = name
        self.description = description
        self.conditional = ""
        self.talkable = talkable

    def talk(self):
        pass

def add_door(direction, room1, room2, locked = False):
    """direction from room 1 to room 2"""
    new_door = Door(room1, room2, locked)
    room1.add_door(direction, new_door)
    room2.add_door(direction, new_door)

def parse(input, player):
    words = input.split(' ')
    room = player.current_room
    for command in commands.keys():
        if command in words:
            if len(command) > 1:
                pass
            else:
                cmd = words[0]
                if cmd == 'look' or cmd == 'l':
                    return look_at(room)
                if cmd == 'i' or cmd == 'inventory':
                    return view_inv(player)

            return "You know how to do that"
    else:
        return "You don't understand how to do that."

def look_at(real):
    return real.description

def use(item1, item2 = None):
    if not item1:
        return item1.use()

def take(item_name, player):
    if item_name in player.current_room.objects.keys():
        item = player.current_room.rm_item(item_name)
        player.add_item(item)
        return "taken"
    return "I don't see that"

def view_inv(player):
    ls = "Inventory:\n"
    items = player.items.keys()
    if len(items) == 0:
        ls += "EMPTY"
        return ls
    for item in player.items.keys():
        ls += item + '\n'
    return ls

def drop(item_name, player):
    if item_name in player.current_room.objects.keys():
        item = player.rm_item(item_name)
        player.current_room.add_item(item)
        return "dropped"
    return "I don't have that"

def quit():
    pass
    
commands = {"look": look_at, "l": look_at,
            "inventory": view_inv, "i": view_inv,
            "take": take, "use": use, "drop": drop,
            "quit": quit(), "q": quit()}

preps = ["to", "at", "on", "for", "from", "@"]

directions = ["north", "east", "south", "west",
                "straight", "right", "back", "left"]  