# Addie Erickson | Unit 1 Final Project

import time

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
if "green" in color or "purple" in color:
    print(f"{color} is my fav too!")
elif "pink" in color:
    print(f"Really? {color}?? Not even a cool shade? I mean you do you I guess...")
else:
    print(f"{color} is quite nice :)")

time.sleep(2)



# age question
while True:
    try:
        age = int(input("How old are you on your home planet?? "))
    except:
        print("Thats not a number!")
    else:
        break

time.sleep(1)

# age question response
if age >= 200:
    print("WOAH, okay grandpa! Does your home planet just move really fast? Either way on Earth your an adult...")
elif age >= 18:
    print("On Earth you are concidered an adult.")
elif age <= 5:
    print("Okay...either your planet moves really slowly or your a baby...both of which are interesting...")
else:
    print("Cool.")

time.sleep(3)



# hobby question
hobby = input("Do you have a hobby that you like to do in your free time? ").lower()

time.sleep(1)

# hobby response
if "running" in hobby or "sports" in hobby or "soccer" in hobby or "basketball" in hobby or "football" in hobby:
    print(f"Oof, yeah {hobby} not for me")
elif "ing" in hobby:
    print(f"Hmm yes, I like {hobby} too.")
else:
    print(f"Oooh, {hobby} seems fun! I should try it :)")

time.sleep(2)



# planet residence question
planet = input("What planet do you live on? Prefreably in our known solar system, intergalactic and interstellar residencies can get complex: ").lower()

time.sleep(1)

# planet residence question response
if "earth" in color:
    print("So your human right?")
elif "pluto" in color:
    print("Same!!")
else:
    print(f"{planet} is quite nice, I've visited before but only seen the most toristy places.")

time.sleep(2)



# SUB QUESTION OF PLANET RESIDENCE QUESTION 

# favorite place on planet question
fav_place = input(f"What is your fav place on {planet}? ").lower()

time.sleep(1)

# favorite place on planet question response
if "jupiter" in planet:
    print(f"Oh guess I'll have to visit {fav_place} on Jupiter. Have you ever been to one of its moons?")
elif "mars" in planet or "neptune" in planet or "uranus" in planet:
    print(f"Is it cold there? I've heard {fav_place} is nice though, guess I'll have to visit!")
else:
    print(f"Ahhh, yes, I've seen {fav_place} its also one of my faves.")

time.sleep(3)



# final output | all together
print(f"Very nice, so your {name} and you are {age} years old and you like to {hobby} and like {color} right? If thats not exactally who you are then theres nothing I can do, good luck on your adventures!")

time.sleep(4)



# end statement
print("Bye, heheheh...")