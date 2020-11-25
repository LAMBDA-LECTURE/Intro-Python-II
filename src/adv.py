from room import Room
from player import Player
from item import Item

# Declare all the rooms
item = {
    "shiny sword": Item("Shiny sword of doom",
                    "Makes you want to cuddle with it.. "),
    "bow": Item("Wooden Bow",
                    "Shoots Arrows of wrath and & vengeance"),
    "lancer": Item("Lancer",
                    "It's a lancer. what did you expect?"),
    "cup": Item("Cup of Everfill",
                    "No matter how hard you try,it's always full"),
    "bong": Item("A Bong",
                    "It's some sort of porcelain art peice..."),
    "snake": Item("Teddy",
                    "Stuffed and NOT cuddle"),
    "potion": Item("of greater healing",
                    "It's some sort of porcelain art peice..."),
}

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     [item['snake'], item["bow"]]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
                [item["bong"]]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                [item["bong"]]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                [item["bong"]]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
                [item["bong"]]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
# this is baue's solution code. idk wtf is goiing on.
player = Player("Josh", room["outside"])
running = True
current_room = None
while(running):
    print(player.current_room.name)
    print(player.current_room.description)

    direction = input("where would you like to go? ")
    if direction == "n" :
        player.current_room = player.current_room.n_to
    elif direction == "s" :
        player.current_room = player.current_room.s_to
    elif direction == "e" :
        player.current_room = player.current_room.e_to
    elif direction == "w" :
        player.current_room = player.current_room.w_to
    elif direction == "a" :
        print(f"you investigate and find {player.current_room.items}")
        action = input("Would you like any of these items? ")
        if action == "y":
            # for index, value in player.current_room.items:
            #     print(f'[{index}]: {value}')
            select_item = int(input("which item would you like? "))
            if len(player.current_room.items) - 1 >= select_item:
                player.pickup(player.current_room.items[select_item])
                # player.current_room.steal(player.current_room.items[select_item])
                player.current_room.steal(items[select_item])
    elif direction == "d" :
        print(f"you investigate your pockets and find {player.items}")
        action = input("Would you like to drop any of these items? ")
        if action == "y":
            for index, value in player.items:
                print(f'[{index}]: {value}')
            select_item = input("which item would you like to drop? ")
            if len(player.items) - 1 > select_item:
                player.drop(player.items[select_item])
                player.current_room.add(player.items[select_item])

    elif direction == "q":
        running = False
    else:
        print("please ender a cardinal direction or q to exit")
        # currently errors out if we go to a none existent room:
    if player.current_room is None:
        print(f"there is nowhere for {player.name} to go that way")
