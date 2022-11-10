class Room:
    def __init__(self, description, north, east, south, west):
        self.description = description

        self.north = north
        self.east = east
        self.south = south
        self.west = west


def create_room_list():
    return [
        Room("You are in a bedroom.\nThere is a hallway to the west and another bedroom to the south.",
             None, None, 3, 1),
        Room("You are in a hallway.\nThere is a bedroom to the west, another hallway to the south, "
             "and a dining room to the east.",
             None, 2, 4, 0),
        Room("You are in a dining room.\nThere is a hallway to the west and a kitchen to the south.",
             None, None, 5, 1),
        Room("You are in a bedroom.\nThere is a hallway to the west and another bedroom to the north.",
             0, None, None, 4),
        Room("You are in a hallway.\nThere is a bedroom to the west, another hallway to the north, a kitchen "
             "to the east, and a balcony to the south.",
             1, 5, 6, 3),
        Room("You are in a kitchen.\nThere is a dining room to the north and a hallway to the west.",
             2, None, None, 4),
        Room("You are on the balcony.\nThere is a hallway to the north.",
             4, None, None, None)]


def try_to_go(action, previous_room, current_room, room_list):
    """
    Tries to perform the action. Assumes that 'action' is lowercase.
    """

    thanks = "Thanks for playing!"
    unknown_action = "I can't understand your action."
    cant_go = "You can't go that way."
    cant_go_to_previous = "You can't go to the previous room."

    if action == "north" or action == "n":
        if current_room.north is None:
            print(cant_go)
        else:
            return current_room, room_list[current_room.north]

    elif action == "east" or action == "e":
        if current_room.east is None:
            print(cant_go)
        else:
            return current_room, room_list[current_room.east]

    elif action == "south" or action == "s":
        if current_room.south is None:
            print(cant_go)
        else:
            return current_room, room_list[current_room.south]

    elif action == "west" or action == "w":
        if current_room.west is None:
            print(cant_go)
        else:
            return current_room, room_list[current_room.west]

    elif action == "back" or action == "b":
        if previous_room is not None:
            return current_room, previous_room
        else:
            print(cant_go_to_previous)

    elif action == "quit" or action == "exit" or action == "q":
        print(thanks)
        return None

    else:
        print(unknown_action)

    return previous_room, current_room


def main():
    room_list = create_room_list()

    previous_room = None
    current_room = room_list[0]

    while True:
        print()
        print(current_room.description)

        action = input("Which direction do you want to go? ").lower()

        previous_room, current_room = try_to_go(action, previous_room, current_room, room_list)

        if current_room is None:
            break


if __name__ == "__main__":
    main()
