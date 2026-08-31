# Addie Erickson | Unit 1 Final Project

import sys
import time

# terms and conditions
print("I'm trusting you to not enter any numbers or random things into the code where there aren't supposed to be, I'll be watching you...")

time.sleep(6)


# agreement question
while True:
    agreement = input("Do you agree to these terms and conditions? ").strip().lower()
    time.sleep(1)
    
# agreement response
    if agreement == "no" or agreement == "nope" or agreement == "nah" or agreement == "" or agreement == "idk" or agreement == "i don't know":
        print("ERROR | UNACCEPTED ANSWER: have fun! heheheheh hahahah")
        sys.exit()
    else:
        print("Welcome, have fun! First off all:")
        break

# name question
name = input("What is your name? ").capitalize()

time.sleep(1)

# name question response
print(f"Hello {name}")

time.sleep(2)



# color question
color = input("What is your favorite color? ").lower()

time.sleep(1)

# color question response 
if "green" in color or "purple" in color or "dark cordovan" in color:
    print(f"{color} is my fav too!")
elif color == "pink":
    print(f"Really? {color}?? Not even a cool shade? I mean you do you I guess...")
else:
    print(f"{color} is quite nice :)")

time.sleep(2)



# age question
while True:
    try:
        age = int(input("How old are you on your home planet?? "))
        time.sleep(1)
    except:
        print("That's not a number!")
    else:
        break

time.sleep(1)

# age question response
if age >= 102:
    print("WOAH! Okay grandpa! Does your home planet just move really fast? Either way on Earth you're an adult...")
elif age >= 18:
    print("On Earth you are considered an adult.")
elif age <= 5:
    print("Okay...either your planet moves really slowly or you're a baby...both of which are concerning...")
else:
    print("Cool.")

time.sleep(3)



# hobby question
while True:
    hobby = input("What is a hobby that you like to do in your free time? ").strip().lower()

    time.sleep(1)

# hobby response
    if hobby == "no" or hobby == "nope" or hobby == "nah" or hobby == "" or hobby == "idk" or hobby == "i don't know":
            print("Alright then, I'm sure you like doing something right?? ")
            time.sleep(1)
    elif hobby in ["running", "sports", "soccer", "basketball", "football"]:
        print(f"Oof, yeah {hobby}s not for me")
        break
    elif "ing" in hobby:
        print(f"Hmm yes, I like {hobby} too.")
        break
    else:
        print(f"Oooh, {hobby} seems fun! I should try it :)")
        break

time.sleep(2)



# planet residence question
planet = input("What planet do you live on? Preferably in our known solar system, intergalactic and interstellar residencies can get complex: ").capitalize()

time.sleep(1)

# planet residence question response
if "Earth" in planet:
    print("So you're human, right? If not, why do you live there?")
elif "Pluto" in planet:
    print("Same!!")
else:
    print(f"{planet} is quite nice, I've visited before but only seen the most touristy places.")

time.sleep(2)



# SUB QUESTION OF PLANET RESIDENCE QUESTION 

# favorite place on planet question
fav_place = input(f"What is your favortie place on {planet}? ").lower()

time.sleep(1)

# favorite place on planet question response
if "jupiter" in planet:
    print(f"Oh guess I'll have to visit {fav_place} on Jupiter. Have you ever been to one of its moons?")
elif "mars" in planet or "neptune" in planet or "uranus" in planet:
    print(f"Is it cold there? I've heard {fav_place} is nice though, guess I'll have to visit!")
else:
    print(f"Ahhh, yes, I've seen {fav_place} it's also one of my faves.")

time.sleep(3)



# srip "ing" from hobby
if hobby.endswith("ing"):
    hobby_verb = hobby[:-3]
else:
    hobby_verb = hobby




# final output | all together
print(f"Very nice, so your {name} and you are {age} years old and you live on {planet} and like to {hobby_verb} and like {color} right? If that's not exactly who you are there's nothing I can do.")

time.sleep(1)

print("Good luck on your adventures!")

time.sleep(8)



# end statement
print("Bye, heheheh...")