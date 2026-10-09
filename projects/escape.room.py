# AE | P1 | Escape Room

import random
import time

# OUTPUT info
# OUTPUT key elements
# GET INPUT choice of either
# IF choice is count coins
    # OUTPUT the box explodes coins everywhere
    # OUTPUT FOR every coin in box, quarters, pennies, dimes, nickles etc.
    # GET INPUT from user of what is the total number of dollars is
# ELIF choice is count carpet
    # FOR every number between chosen code 
        # OUTPUT the numbers between and after
    # IF number gets passed 500
        # OUPUT you are falling asleep
        # IF user INPUTS wake up wake up!
            # continue
        # ELIF user does not and 2 seconds pass 
            # restart counting
        # ELSE
            # restart counting
# ELIF choice is bookshelf
    # OUTPUT books (like actual books that i find that are open source)
    # OUTPUT numbers that arent spelled out and that is the number
# ELIF choice is enter code
    # OUPUT are you sure you wnat to?
        # IF INPUT is yes
            # OUPUT okay
            # GET code from user
# ELIF choice is paper on floor
    # OUTPUT the paper is stained and you can barley make out the faint writing of some numbers
    # OUPUT the numbers are: 1000
# ELSE
    # OUTPUT you sit in the room, pondering your existance
# IF user inputs correct number into phone
    # OUPUT get out
# ELIF user INPUTS wrong number 2 times
    # OUPUT hint: would you like too try to look around the room and examine the objects provided?
        # IF hint is yes list objects again and let choose
# ELSE
    # OUTPUT hehe your stuck forever!!
    # break / exit code

codes_bookshelf = [2356, 9990, 8031, 6574, 8383, 3333, 6753, 6994, 9393, 676767676767]

coins_codes = [7151, 5890, 3373, 1643, 6869]

carpet_codes = [200601, 288060, 356083, 555556, 676767]

self_destruct_code = [1000]

print("You are stuck within a escape room")
time.sleep(2)
print("You have infinite time but only 3 tries to enter the correct code and get out")
time.sleep(4)
print("Good luck")
time.sleep(1)

print("You are in a room, this room is mostly bare exept for a old rotary phone where you will enter the code to escape")

time.sleep(5)

print("A few key elements within the room:")
time.sleep(1.5)
print("- a bookshelf with 3 books")
time.sleep(1)
print("- a box filled with an unknown number of different coins")
time.sleep(2)
print("- the carpet on the floor")
time.sleep(1)
print("- some papers on the floor")
time.sleep(1)

# while True loop
choice = input("What would you like to examine? [COINS / CARPET / BOOKSHELF / PAPERS / PHONE] ").strip().lower()

if choice == "coins":
    print("As you approach the box of coins it bursts open, coins flying everywhere")
    time.sleep(.5)
    coins_choice = input("What would you like to do with the coins? [EAT / COUNT / THROW / LAY] ").strip().lower()
    if coins_choice == "eat":
        print("You eat a couple coins before choking, everything goes black...")
        time.sleep(2)
        # send back up to first output
    elif coins_choice == "throw":
        print("Okay child, you throw the coins and one hits you, now what do you want to do with them?")
        time.sleep(.5)
        # send back to coins_choice
    elif coins_choice == "lay":
        print("Layin in the coins feels nice and cold, you begin to fall asleep...")
        time.sleep(2)
        # send back to coins_choice
    elif coins_choice == "count":
        print("You begin to count the coins...")
        time.sleep(2)
        # for loop counting each individual coin, quarter, penny etc.
        # randomize number of each to equal one of the codes above for coins_codes
        # have user add all the dollars together to get code
    else:
        print("No, that is not one of the choices")
        time.sleep(.5)
elif choice == "carpet":
    # for every number between chosen code from carpet_codes print
    # if number gets passed 500
        # print("You are fallin asleep")
        # IF user INPUTS wake up wake up!
            # continue
        # ELIF user does not and 2 seconds pass 
            # restart counting & code
        # ELSE
            # restart counting & code
    print("")
elif choice == "bookshelf":
    print("You pick up one of the books titiled \"A Cristmas Carol\"")
    read_cc = input("Would you like to read it? [YES / NO] ").strip().lower()
    if read_cc == "yes" or read_cc == "y":
        print("Title: A Christmas Carol")
        print("Author: Charles Dickens")
        print("Release date: December 24, 2007 [eBook #24022]")
        print("    Most recently updated: August 9, 2012")
    elif read_cc == "no" or read_cc == "n":