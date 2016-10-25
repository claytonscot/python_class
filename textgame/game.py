__author__ = 'Home'
def main ():
    name = get_name()
    race = get_race()
    race_profile = get_profile(race)

    print("Welcome to the world, ", name, ". You are a ", race, ", which means\n", race_profile, "Good luck on your quest...\n", sep="")

    if race == "human":
        human_quest(name)
    elif race == "gherkin":
        gherkin_quest(name)
    else:
        giant_quest()

#Profile functions
def get_name():
    name = input("What is your name?")
    return name
def get_race():
    race = input("What kind of creature are you?\nhuman\ngherkin\ngiant\n:")
    return race
def get_profile(race):
    print(race)

    if race == "human":
        return "you are of average size. You are at home in the fresh air;\n" \
               "wind in your sails, dirt on your boots, and dreams of the sky.\n" \
               "You enjoy the fellowship of the people all around.\n"
    if race == "gherkin":
        return "you are a very small creature. You care deeply about the earth\n" \
               "and its inhabitants, particularly insects and rodents.\n"
    if race == "giant":
        return "you are so large a cave is your only means of shelter, if you can find one.\n" \
               "Your size results in you being a deeply misunderstood creature with a natural\n" \
               "drive towards unintentional destruction. You find yourself accidentally causing\n" \
               "all kinds of mayhem. Sitting down could mean the death of several villagers."

#Human Quest
def human_quest(name):
    print("You are Captain ", name,". After a horriffic pirate attack, you wash up on the shore.\n"
                                   "As far as you know, your crew was slaughtered. The last thing\n"
                                   "you remember before passing out was a pillar of smoke coming\n"
                                   "from your ship as you tied yourself desperately to an empty barrel.\n\n", sep="")
    print("(look)  (get)  (north)  (south)  (east)")
    action = input(":")

#Gherkin Quest
def gherkin_quest(name):
    inventory = ["n","n","n","n"]

    loc = "y_3"
    print("You are Prince ", name,", of the Kemlich clan in the lower granite halls of Ablemec.\n"
            "Your father is concerned about the state of the forest above the kingdom of the\n"
            "Kelonite gherkins, your allies to the north. The trees there are dying and Jeemlim\n"
             "is in short supply. You have been given the task of investigating the forest.\n")
    if loc == "y_3":
        y_3(inventory)

def y_3(inventory):
    here = True
    print("\n\nY-3: The Basin Chamber")
    print("(look)  (get)  (east)")
    print("A natural cutout in the earth from worms.")
    while here == True:


        action = input(":")
        if action == "look" and inventory[0] == "n":
            print("Gherkins come to the Basin Chamber to gauge the activity of local\n"
                  "earthworms. Humidity and worm droppings reveal conditions of the world above.\n"
                  "The entrance is to the east. Your favorite shale sled is waiting in the corner.")
        elif action == "look":
            print("Gherkins come to the Basin Chamber to gauge the activity of local\n"
                  "earthworms. Humidity and worm droppings reveal conditions of the world above.\n"
                  "The entrance is to the east.")
        elif action == "get" and inventory[0] == "n":
            print("You got the shale sled!")
            inventory[0] = "y"
        elif action == "get" and inventory[0] == "y":
            print("You already have the sled. Show some gratitude.")
        elif action == "east":
            y_4(inventory)
        else:
            print("whatever")

def y_4(inventory):
    here = True
    print("\n\nY-4: Shale Road. Basin Chamber")
    if inventory[0] == "y":
        print("(look)  (get)  (north)  (south)  (west)  (sled)")
    else:
        print("(look)  (get)  (north)  (south)  (west)")
    while here == True:
        action = input(":")
        if action == "look":
            print("A section of the South Shale Road. The entrance to the Basin Chamber\n"
                  "lies to the west.")
        elif action == "get":
            print("There is nothing to get")
        elif action == "west":
            y_3(inventory)
        elif action == "east":
            print("You slam into the rocky wall but get nowhere.")
        elif action == "south":
            z_4(inventory)

def z_4(inventory):
    here = True
    print("\n\nZ-4: Shale Road. Granite Halls")
    if inventory[0] == "y":
        print("(look)  (get)  (north)  (south)  (east)  (sled)")
    else:
        print("(look)  (get)  (north)  (south)  (east)")
    while here == True:
        action = input(":")
        if action == "look":
            print("The southernmost section of the South Shale Road.\n"
                  "The Granite Halls lie to the east")
        elif action == "east":
            z_5(inventory)
        elif action == "north":
            y_4(inventory)

def z_5(inventory):
    here = True
    print("\n\nZ-5: Granite Halls.")
    if inventory[0] == "y":
        print("(look)  (get)   (north)   (south)    (east)    (west)    (sled)")
        print("               -Library-  -Store-    -Road-  -Royal Fort-")
    else:
        print("(look)  (get)   (north)   (south)     (east)     (west)")
        print("               -Library-  -Store-  -Royal Fort-  -Road-")
    while here == True:
        action = input(":")
        if action == "look":
            print("The great Granite Halls of Ablemec. The home of your father\n"
                  "and your father's father. A small but noble town.")
        elif action == "east":
            z_6(inventory)
        elif action == "south":
            store(inventory)
        elif action == "west":
            z_4(inventory)

def z_6(inventory):
    here = True
    print("\n\nZ-6: Ablemec Royal Fortress")
    print("(look)   (north)    (west)  ")
    print("       -Throne Rm-  -Town- ")
    while here == True:
        action = input(":")
        if action == "west":
            z_5(inventory)
        elif action == "look":
            print("The Royal Fortress of Ablemec. A peaceful, but well-protected gherkin fort.\n"
                    "Ruled by King Minar III. Center of all southern gherkin intelligence. The\n"
                    "throne room is north, but a guard stands by.")


def store(inventory):
    print("Welcome to Wheelock's General Store")
    print("(buy)   (sell)   (talk)   (leave)")
    here = True
    while here == True:
        action = input(":")
        if action == "sell":
            print(inventory)
        elif action == "leave":
            z_5(inventory)





main()

