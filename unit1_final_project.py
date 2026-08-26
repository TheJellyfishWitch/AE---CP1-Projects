# Addie Erickson | Unit 1 Final Project

# variables
color = input("What is your favorite color?").lower()
name = input("What is your name?").lower()
age = input("How old are you??")
hobby = input("Do you have a hobby that you like to do in your free time?").lower()
planet = input("What planet do you live on? Prefreably in our known solar system, intergalactic and interstellar residencies can get complex.").lower()

# color question response
if "green" in color or "orange" in color:
    print(color, " is mine too!")
elif "pink" in color:
    print("Really? ", color, "?? Not even a cool shade?")
else:
    print(color, " is quite nice :)")