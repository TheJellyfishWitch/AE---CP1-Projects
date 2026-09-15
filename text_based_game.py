# AE | P1 | Text Game

import time

# say hello
# GET user name
# SET setting
# GET user input, tavern or forest
# TAVERN
    # user food
    # user sleep
    # user
# russian routlette

# endings
    # you ate fairy food and danced forever more

# INPUT | name
name = input("Hi what is your name: ").title()
print(f"Hello {name} do you agree to at least try to input ")

# CHOICE | OUTSIDE | tavern / forest
while True: 
    tavern_forest = input("You are on an adventure, would you like to go to the TAVERN or the FOREST? ").lower()
# CHOICE | TAVERN | food
    if tavern_forest == "tavern":
        print("You are heading into the tavern, it is warm and cozy. Whispered chatter echoes in the background, tables line the room, people are dancing breathless.")
        time.sleep(7)
        print("A bar is set up with food and drink, the tender says, \"The food is good.\"")
        time.sleep(1)
        check_bartender = input("Do you check the bartender? [YES / NO] ").lower()
        break
# CHOICE | FOREST | conversation, figure
    elif tavern_forest == "forest":
        print("You head into the woods, trees cut out the stars and only the moon lights your path. The trail is smooth and good for walking.")
        time.sleep(6)
        forest_conversation = input("A shadowy figure leaves the trees and begins to walk ahead of you, do you strike up a conversation? [YES / NO] ").lower()
        break
    else:
        print("That is not an accepted answer, try again.")

# CHECK | TAVERN | bartender
if check_bartender == "yes":
    print("Something is off about him, his teeth are overly sharp and his hands look more like claws and there is something shimmery about his skin...")
    time.sleep(7)
    tavern_food = input("Do you partake of the food? [YES / NO] ").lower()
else:
    tavern_food = input("Do you partake of the food? [YES / NO] ").lower()

# END | TAVERN | fairy food
if tavern_food == "yes":
    print("Famished you partake of the food, grabbing both the drink and the cheese. Something weird comes over you,")
    time.sleep(4)
    print("A sudden desire to dance! And dance you begin...")
    time.sleep(2)
    print("STORY END: you ate fairy food and danced forever more")
# 
else:
    print("Those around you start to change, hands change sharp and blue, teeth become fangs and they start to growl. Fairies!")
    time.sleep(6)
    tavern_run = input("Do you run out of the tavern? [YES / NO] ").lower()