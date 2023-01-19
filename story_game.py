### STORY GAME ###

#LEVEL1

print("""

Welcome to the Python Story Game!
You find yourself in a dark forest, 
and you need to find your way out.

""")

level1_true = True

while level1_true == True:
    # Get user input for direction
    print("Which direction do you want to go? (north, south, east, west)")
    direction = input()

    # Determine outcome based on user input
    if direction == "north":
        print("You find a path that leads you out of the forest. You have escaped!")
        level1_true = False
    elif direction == "south": 
        print("You come across a swamp and get lost. Game over. Try again.")
    elif direction == "east":
        print("You find a river and manage to follow it out of the forest. You have escaped!")
        level1_true = False
    elif direction == "west":
        print("You met a bear and now you have to choose between RUNNING or PRETENDING TO BE DEAD? Enter your choice:")
        choice = input()
        if choice == "running":
            print("The bear caught up with you. I'm sorry. make practice and try again.")
        elif choice == "pretending to be dead":
            print("You're a great actor, man. The bear believed you and left. Congratulations, you completed level1!")
            level1_true = False
    else:
        print("I don't understand your choice. Try again.")

#LEVEL2

print("""

Congratulations on escaping the forest! You find yourself in a desert. 
You need to find water to survive.

""")

level2_true = True

while level2_true == True:
    # Get user input for direction
    print("Which direction do you want to go? (north, south, east, west)")
    directions = input()

    # Determine outcome based on user input
    if directions == "north":
        print("You find an oasis and live happily ever after.")
        level2_true = False
    elif directions == "south":
        print("You find a mirage and die of dehydration. Game over.")
        level2_true = False
    elif directions == "east":
        print("You find a hidden cave with water and survive. You have escaped the desert!")
        level2_true = False
    else:
        print("You find a sandstorm and can't find your way out. Try again.")


