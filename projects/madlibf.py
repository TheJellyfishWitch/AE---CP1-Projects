# Addie Erickson | Madlib

import time

# input variables
user_name = input("Enter your name: ").capitalize()
name = input("Enter a name: ").capitalize()
room = input("Enter a room: ").lower()
place = input("Enter a place: ").capitalize()
judge = input("Enter a name: ").capitalize()
food = input("Enter a food: ").lower()
ingrediant = input("Enter an ingrediant: ").lower().lower()
verb_ing = input("Enter a verb ending in 'ing': ").lower()
verb_two = input("Enter a verb: ").lower()
country = input("Enter a country [ex: british, greek]: ").capitalize()
meat = input("Enter a form of meat: ").lower()
veggie = input("Enter a vegatable: ").lower()
while True:
    try:
        number = int(input("Enter a number: "))
    except:
        print("thats not a number!!")
    else:
        break
adjective = input("Enter a adjective: ").lower()
verb_four = input("Enter a verb: ").lower()

# final statment
print(f"Welcome back to the annual cooking competition final round, this years round we have {user_name} vs. {name}!")
time.sleep(3)
print(f"This years game is hosted in {room} of {place}, our judge is {judge}.")
time.sleep(2)
print(f"'Hello, hello! Today our contestants will be making {food} with our special ingrediant: {ingrediant}!'")
time.sleep(3)
print(f"You all have {number} of hours, begin!' You and {name} get to work, you start by {verb_ing} to grab your pot.")
time.sleep(5)
print(f"Looking over {name} {verb_two} a bowl and starts to cook.")
time.sleep(2)
print(f"You and {name} started adding {country} {meat}, you also added some {veggie} and the {ingrediant}.")
time.sleep(3)
print(f"'Alright contestants, your time is up!' {judge} said, {judge} tried your dish first. {judge} replies with 'your dish is very {adjective}'. Then {judge} tried {name}'s dish, 'This is incredible, it's {verb_four}' {judge} said smiling.")
time.sleep(8)
print(f"'Drum roll please, {name} wins!!'")
time.sleep(2)
print("You lost :(")

