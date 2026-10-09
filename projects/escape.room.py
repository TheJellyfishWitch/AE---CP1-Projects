# AE | P1 | Escape Room

import random
import time
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

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

codes = [2356, 9990, 8031, 6574, 8383, 3333, 6753, 6994, 9393, 676767676767]

codes_bookshelf = [24022]


coins_codes = [7151, 5890, 3373, 1643, 6869]

carpet_codes = [200601, 288060, 356083, 555556, 676767]

self_destruct_code = [1000]

print("You are stuck within a escape room")
time.sleep(2)
print("You have infinite time but only 3 tries to enter the correct code and get out")
time.sleep(4)
print("Good luck")
time.sleep(1)

clear_terminal()

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

clear_terminal()

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
    time.sleep(1)
    read_cc = input("Would you like to read it? [YES / NO] ").strip().lower()
    if read_cc == "yes" or read_cc == "y":
        print("Title: A Christmas Carol")
        time.sleep(1)
        print("Author: Charles Dickens")
        time.sleep(1)
        print("Release date: December, Twenty-Fourth, Two-thousand-seven [eBook #24022]")
        time.sleep(1)
        print("[Most recently updated: August, Ninth, Twenty-Twelve]")
        time.sleep(1)
        print("Language: English")
        time.sleep(1)
        print("Origional publication: Philadelphia and New York: J. B. Lippincott Company,, Ninteen-Fifteen")
        time.sleep(3)
        print("Credits: Produced by Suzanne Shell, Janet Blenkinship and the Online")
        time.sleep(2)
        print("Link to eBook: https://www.gutenberg.org/files/46/46-h/46-h.htm")
        time.sleep(2)

        clear_terminal()

        print("PREFACE")
        time.sleep(1)
        print("I have endeavoured in this Ghostly little book to raise the Ghost of an Idea which shall not put my readers out of humour with themselves, with each other, with the season, or with me. May it haunt their house pleasantly, and no one wish to lay it.\n"
        "Their faithful Friend and Servant,\n"
        "C. D.\n" 
        "December, Eighteen-Fourty-three.")
        time.sleep(9)

        clear_terminal()

        print("CHARACTERS")
        time.sleep(1)
        print("Bob Cratchit, clerk to Ebenezer Scrooge.\n"
        "Peter Cratchit, a son of the preceding.\n"
        "Tim Cratchit (\"Tiny Tim\"), a cripple, youngest son of Bob Cratchit.\n"
        "Mr. Fezziwig, a kind-hearted, jovial old merchant.\n"
        "Fred, Scrooge's nephew.\n"
        "Ghost of Christmas Past, a phantom showing things past.\n"
        "Ghost of Christmas Present, a spirit of a kind, generous, and hearty nature.\n"
        "Ghost of Christmas Yet to Come, an apparition showing the shadows of things which yet may happen.\n"
        "Ghost of Jacob Marley, a spectre of Scrooge's former partner in business.\n"
        "Joe, a marine-store dealer and receiver of stolen goods.\n"
        "Ebenezer Scrooge, a grasping, covetous old man, the surviving partner of the firm of Scrooge and Marley.\n"
        "Mr. Topper, a bachelor.\n"
        "Dick Wilkins, a fellow apprentice of Scrooge's.\n"
        "\n"
        "Belle, a comely matron, an old sweetheart of Scrooge's.\n"
        "Caroline, wife of one of Scrooge's debtors.\n"
        "Mrs. Cratchit, wife of Bob Cratchit.\n"
        "Belinda and Martha Cratchit, daughters of the preceding.\n"
        "\n"
        "Mrs. Dilber, a laundress.\n"
        "Fan, the sister of Scrooge.\n"
        "Mrs. Fezziwig, the worthy partner of Mr. Fezziwig.")
        time.sleep(14)

        clear_terminal()

        print("CONTENTS")
        time.sleep(1)
        print("STAVE ONE- Marley's Ghost")
        time.sleep(1)
        print("STAVE TWO - The First of the Three Spirits")
        time.sleep(1)
        print("STAVE THREE - The Second of the Three Spirits")
        time.sleep(1)
        print("STAVE FOUR - The Last of the Spirits")
        time.sleep(1)
        print("STAVE FIVE - The End of It")
        time.sleep(1)

        clear_terminal()

        print("---------------")
        print("   STAVE ONE")
        print("---------------")

    elif read_cc == "no" or read_cc == "n":
        print("")