#!/usr/bin/env python
# coding: utf-8

# define rooms and items

#furniture
couch = {
    "name": "couch",
    "type": "furniture",
}

double_bed = {
    "name": "double bed",
    "type": "furniture",
}

queen_bed = {
    "name": "queen bed",
    "type": "furniture",
}

dresser = {
    "name": "dresser",
    "type": "furniture",
}

dining_table = {
    "name": "dining table",
    "type": "furniture",
}

piano = {
    "name": "piano",
    "type": "furniture",
}

piggybank = { #added dict for extra riddle
    "name": "piggybank",
    "type": "furniture", 
}

clip = { #added dict for extra riddle
    "name": "clip",
    "status": False
}

#doors
door_a = {
    "name": "door a",
    "type": "door",
    "state": "closed" #added for doors staying open
}
door_b = {
    "name": "door b",
    "type": "door",
    "state": "closed" #added for doors staying open
}
door_c = {
    "name": "door c",
    "type": "door",
    "state": "closed" #added for doors staying open
}
door_d = {
    "name": "door d",
    "type": "door",
    "state": "closed" #added for doors staying open
}

#keys
key_a = {
    "name": "key for door a",
    "type": "key",
    "target": door_a,
}
key_b = {
    "name": "key for door b",
    "type": "key",
    "target": door_b,
}
key_c = {
    "name": "key for door c",
    "type": "key",
    "target": door_c,
}
key_d = {
    "name": "key for door d",
    "type": "key",
    "target": door_d,
}



#rooms
game_room = {
    "name": "game room",
    "type": "room",
    "image_path": r'images\GameRoom.png', #added for images showing
}

bedroom1 = {
    "name": "bedroom 1",
    "type": "room",
    "image_path": r'images\Bedroom1.png', #added for images showing
}

bedroom2 = {
    "name": "bedroom 2",
    "type": "room",
    "image_path": r'images\Bedroom2.png', #added for images showing
}

living_room = {
    "name": "living room",
    "type": "room",
    "image_path": r'images\LivingRoom.png', #added for images showing
}

outside = {
  "name": "outside",
  "image_path": r'images\Outside.png', #added for images showing
}

all_rooms = [game_room, bedroom1, bedroom2, living_room, outside]

all_doors = [door_a, door_b, door_c, door_d]

# define which items/rooms are related

object_relations = {
    "game room": [couch, piano, door_a],
    "bedroom 1": [queen_bed, door_a, door_b, door_c, piggybank], #added piggybank for extra riddle
    "bedroom 2": [double_bed, dresser, door_b],
    "living room": [dining_table, door_c, door_d],
    "outside": [door_d],
    "piano": [key_a],
    "queen bed": [key_b],
    "double bed": [key_c],
    "dresser": [key_d],
    "piggybank": [clip], #added for extra riddle
    "door a": [game_room, bedroom1],
    "door b": [bedroom1, bedroom2],
    "door c": [bedroom1, living_room],
    "door d": [living_room, outside]
}

# define game state. Do not directly change this dict. 
# Instead, when a new game starts, make a copy of this
# dict and use the copy to store gameplay state. This 
# way you can replay the game multiple times.

INIT_GAME_STATE = {
    "current_room": game_room,
    "keys_collected": [],
    "target_room": outside
}

from add_on_images import show_an_image
#show_an_image(r'images\img1.png')

from add_on_shake_it import shake_it
#clip = shake_it()

from suspense_text import suspense_text
#suspense_text("text")

from colorama import Fore, Style
#suspense_text(Fore.RED +"this is red " + Style.RESET_ALL + "this is normal")

def postcredits(clip):
    if clip["status"] == True:
        suspense_text("You see the last moments of the sunset. You can finally breathe. However, a SUPER SUSPICIOUS man approaches you. Without any doubt, you wave to a car that is passing by and enter the vehicle. You breathe a sigh of relief, only for you to find out that the driver" + Fore.RED +  " ITS HIM! THE DOORS LOCK, YOUR HEART RACES AND THE MAN LAUGHS" + Style.RESET_ALL + "…. But there is hope! You remember the clip you found in the first room! You take it, put it against the door and manage to unlock it! You get out of the car and run as fast as you can. Maybe you are safe now… but just maybe…" + Style.RESET_ALL)
    else:
        suspense_text("You see the last moments of the sunset. You can finally breathe. However, a SUPER SUSPICIOUS man approaches you. Without any doubt, you wave to a car that is passing by and enter the vehicle. You breathe a sigh of relief, only for you to find out that the driver" + Fore.RED +  " ITS HIM! THE DOORS LOCK, YOUR HEART RACES AND THE MAN LAUGHS" + Style.RESET_ALL + " … You desperately try to get out, but you can't. Your fate is now sealed…" + Fore.RED + " FOREVERRRRR" + Style.RESET_ALL)


def linebreak():
    """
    Print a line break
    """
    print("\n\n")

def start_game():
    """
    Start the game
    """
    suspense_text("A loud crackling noise wakes you up - KA-CHUNK-CREEEEEAK. As you get your senses back, with your vision still blurred, you find yourself in a dark room." + Fore.RED +" 'Wh-Where am I?'" + Style.RESET_ALL + " Well, that's a good question. Up to you to find out …Oh, but do worry … because" + Fore.RED + " HE IS COMING BACK!     \n"+ Style.RESET_ALL)
    play_room(game_state["current_room"])

def play_room(room):
    """
    Play a room. First check if the room being played is the target room.
    If it is, the game will end with success. Otherwise, let player either 
    explore (list all items in this room) or examine an item found here.
    """
    game_state["current_room"] = room
    if(game_state["current_room"] == game_state["target_room"]):
        print("Congrats! You escaped the room!")
        postcredits(clip)
    else:
        print("You are now in " + room["name"])
        intended_action = input("What would you like to do? Type 'a' for exploring or 'b' for examining?").strip() #changed
        if intended_action.lower() == "a":#changed
            explore_room(room)
            play_room(room)
        elif intended_action.lower() == "b":#changed
            examine_item(input("What would you like to examine?").strip())
        else:
            print("Not sure what you mean. Type 'a' for exploring or 'b' for examining.")#changed
            play_room(room)
        linebreak()

def explore_room(room):
    """
    Explore a room. List all items belonging to this room.
    """
    items = [i["name"] for i in object_relations[room["name"]]]
    print("You explore the room. This is " + room["name"] + ". You find " + ", ".join(items))

def get_next_room_of_door(door, current_room):
    """
    From object_relations, find the two rooms connected to the given door.
    Return the room that is not the current_room.
    """
    connected_rooms = object_relations[door["name"]]
    for room in connected_rooms:
        if(not current_room == room):
            return room

def examine_item(item_name):
    """
    Examine an item which can be a door or furniture.
    First make sure the intended item belongs to the current room.
    Then check if the item is a door. Tell player if key hasn't been 
    collected yet. Otherwise ask player if they want to go to the next
    room. If the item is not a door, then check if it contains keys.
    Collect the key if found and update the game state. At the end,
    play either the current or the next room depending on the game state
    to keep playing.
    """
    current_room = game_state["current_room"]
    next_room = ""
    output = None
    item_name = item_name.lower() #added for case insensitive input
    for item in object_relations[current_room["name"]]:
        if(item["name"] == item_name):
            output = "You examine " + item_name + ". "
            if(item["type"] == "door"):
                have_key = False
                for key in game_state["keys_collected"]:
                    if(key["target"] == item):
                        have_key = True
                if item["state"] == "closed":    #added for doors staying open
                    if(have_key):
                        output += "You unlock it with a key you have."
                        item["state"] = "open"   #changed for doors staying open
                        next_room = get_next_room_of_door(item, current_room)
                    else:
                        output += "It is locked but you don't have the key."
                else:                            #changed for doors staying open
                    next_room = get_next_room_of_door(item, current_room)   #changed for doors staying open
            else:
                if(item["name"] in object_relations and len(object_relations[item["name"]])>0):
                    #changes if the item is the piggy bank:
                    if item["name"] == "piggybank" and clip["status"] == False:
                        #start the shake function, save the result into a variable clip and give an output message
                        clip["status"] = shake_it()
                        if clip["status"] == True:
                            output += "You pocket the paper clip."
                    elif item["name"] == "piggybank" and clip["status"] == True:
                        output += "You already shook the piggybank, now it's empty."
                    #else the normal code moved into the else here
                    else:
                        item_found = object_relations[item["name"]].pop()
                        game_state["keys_collected"].append(item_found)
                        output += "You find " + item_found["name"] + "."
                else:
                    output += "There isn't anything interesting about it."
            print(output)
            break

    if(output is None):
        print("The item you requested is not found in the current room.")
    
    if(next_room and input("Do you want to go to the next room? Enter 'yes' or 'no'").strip() == 'yes'):
        show_an_image(next_room["image_path"]) #added to show images
        play_room(next_room)
    else:
        play_room(current_room)




game_state = INIT_GAME_STATE.copy()

start_game()




