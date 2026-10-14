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
    # OUPUT the numbers are: 1001
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

codes = ["2356", "9990", "8031", "6574", "8383", "3333", "6753", "6994", "9393", "676767676767"]

codes_bookshelf = ["24022"]

coins_codes = ["7151", "5890", "3373", "1643"]

carpet_codes = ["200601", "288060", "356083", "555556"]

self_destruct_code_paper = ["1001"]

tries = 3

count_carpet = False

clear_terminal()

print("You are stuck within a escape room")
time.sleep(2)
print("You have infinite time but only three tries to enter the correct code and get out")
time.sleep(4)
print("Good luck")
time.sleep(1)

clear_terminal()

print("You are in a room, this room is mostly bare except for a old rotary phone where you will enter the code to escape")

time.sleep(4)

print("A few key elements within the room:")
time.sleep(1.5)
print("- a bookshelf with one book")
time.sleep(1)
print("- a box filled with an unknown number of different coins")
time.sleep(2)
print("- the carpet on the floor")
time.sleep(1)
print("- some papers on the floor")
time.sleep(1)

while True:
    choice = input("What would you like to examine? [COINS / CARPET / BOOKSHELF / PAPERS / PHONE] ").strip().lower()

    clear_terminal()

    if choice == "coins":
        print("As you approach the box of coins it bursts open, coins flying everywhere")
        time.sleep(2)
        while True:
            coins_choice = input("What would you like to do with the coins? [EAT / COUNT / THROW / LAY] ").strip().lower()
            if coins_choice == "eat":
                print("You eat a couple coins before choking, everything goes black...")
                time.sleep(2)
                print("YOU FAILED!")
                exit()
            elif coins_choice == "throw":
                print("Okay child, you throw the coins and one hits you, now what do you want to do with them?")
                time.sleep(.5)
            elif coins_choice == "lay":
                print("Layin in the coins feels nice and cold, you begin to fall asleep...")
                time.sleep(2)
                print("You wake with a start! NO! You have to escape the room!")
            elif coins_choice == "count":
                print("You begin to count the coins...")
                time.sleep(2)

                random_coin_code = random.choice(coins_codes)

                if random_coin_code == "7151":
                    quarters = 13874
                    count_quarters = 0
                    # ($3,468.50)
                    print("Counting quarters...")
                    while count_quarters < quarters:
                        count_quarters += 2000
                        if count_quarters > quarters: 
                            count_quarters = quarters
                        print(count_quarters)
                    print(f"{quarters} in total")

                    dimes = 16375
                    count_dimes = 0
                    # ($1,637.50)
                    print("Counting dimes...")
                    while count_dimes < dimes:
                        count_dimes += 2500
                        if count_dimes > dimes: 
                            count_dimes = dimes
                        print(count_dimes)
                    print(f"{dimes} in total")
                    
                    nickles = 18847
                    count_nickles = 0
                    # ($942.35)
                    print("Counting nickles...")
                    while count_nickles < nickles:
                        count_nickles += 3000
                        if count_nickles > nickles: 
                            count_nickles = nickles
                        print(count_nickles)
                    print(f"{nickles} in total")

                    pennies = 110295
                    count_pennies = 0
                    # ($1,102.65)
                    print("Counting pennies...")
                    while count_pennies < pennies:
                        count_pennies += 20000
                        if count_pennies > pennies: 
                            count_pennies = pennies
                        print(count_pennies)
                    print(f"{pennies} in total")
                    print("The amount of coins presented to you have been counted :)")
                    time.sleep(2)
                    print("Are you going to be adding them up to get the total amount of dollars?")
                    time.sleep(4)
                    break                
                elif random_coin_code == "5890":
                    quarters_second = 8416
                    count_quarters_second = 0
                    # ($2,104.00)
                    print("Counting quarters...")
                    while count_quarters_second < quarters_second:
                        count_quarters_second += 1000
                        if count_quarters_second > quarters_second: 
                            count_quarters_second = quarters_second
                        print(count_quarters_second)
                    print(f"{quarters_second} in total")

                    dimes_second = 12307
                    # ($1,230.70)
                    count_dimes_second = 0
                    print("Counting dimes...")
                    while count_dimes_second < dimes_second:
                        count_dimes_second += 2000
                        if count_dimes_second > dimes_second: 
                            count_dimes_second = dimes_second
                        print(count_dimes_second)
                    print(f"{dimes_second} in total")
                    
                    nickles_second = 9585
                    count_nickles_second = 0
                    # ($479.25)
                    print("Counting nickles...")
                    while count_nickles_second < nickles_second:
                        count_nickles_second += 1000
                        if count_nickles_second > nickles_second: 
                            count_nickles_second = nickles_second
                        print(count_nickles_second)
                    print(f"{nickles_second} in total")

                    pennies_second = 207605
                    count_pennies_second = 0
                    # ($2,076.05)
                    print("Counting pennies...")
                    while count_pennies_second < pennies_second:
                        count_pennies_second += 30000
                        if count_pennies_second > pennies_second: 
                            count_pennies_second = pennies_second
                        print(count_pennies_second)
                    print(f"{pennies_second} in total")
                    print("The amount of coins presented to you have been counted :)")
                    time.sleep(2)
                    print("Are you going to be adding them up to get the total amount of dollars?")
                    time.sleep(4)
                    break
                elif random_coin_code == "3373":
                    quarters_third = 9329
                    count_quarters_third = 0
                    # ($2,332.25)
                    print("Counting quarters...")
                    while count_quarters_third < quarters_third:
                        count_quarters_third += 3000
                        if count_quarters_third > quarters_third: 
                            count_quarters_third = quarters_third
                        print(count_quarters_third)
                    print(f"{quarters_third} in total")

                    dimes_third = 4181
                    # ($418.10)
                    count_dimes_third = 0
                    print("Counting dimes...")
                    while count_dimes_third < dimes_third:
                        count_dimes_third += 500
                        if count_dimes_third > dimes_third: 
                            count_dimes_third = dimes_third
                        print(count_dimes_third)
                    print(f"{dimes_third} in total")
                    
                    nickles_third = 8027
                    # ($401.35)
                    count_nickles_third = 0
                    print("Counting nickles...")
                    while count_nickles_third < nickles_third:
                        count_nickles_third += 3000
                        if count_nickles_third > nickles_third: 
                            count_nickles_third = nickles_third
                        print(count_nickles_third)
                    print(f"{nickles_third} in total")
                    
                    pennies_third = 22130
                    # ($221.30)
                    count_pennies_third = 0
                    print("Counting pennies...")
                    while count_pennies_third < pennies_third:
                        count_pennies_third += 2000
                        if count_pennies_third > pennies_third: 
                            count_pennies_third = pennies_third
                        print(count_pennies_third)
                    print(f"{pennies_third} in total")
                    print("The amount of coins presented to you have been counted :)")
                    time.sleep(2)
                    print("Are you going to be adding them up to get the total amount of dollars?")
                    time.sleep(4)
                    break
                elif random_coin_code == "1643":
                    quarters_fourth = 3272
                    count_quarters_fourth = 0
                    # ($818.00)
                    print("Counting quarters...")
                    while count_quarters_fourth < quarters_fourth:
                        count_quarters_fourth += 500
                        if count_quarters_fourth > quarters_fourth: 
                            count_quarters_fourth = quarters_fourth
                        print(count_quarters_fourth)
                    print(f"{quarters_fourth} in total")

                    dimes_fourth = 3440
                    # ($344.00)
                    count_dimes_fourth = 0
                    print("Counting dimes...")
                    while count_dimes_fourth < dimes_fourth:
                        count_dimes_fourth += 500
                        if count_dimes_fourth > dimes_fourth: 
                            count_dimes_fourth = dimes_fourth
                        print(count_dimes_fourth)
                    print(f"{dimes_fourth} in total")
                    
                    nickles_fourth = 4810
                    # ($240.50)
                    count_nickles_fourth = 0
                    print("Counting nickles...")
                    while count_nickles_fourth < nickles_fourth:
                        count_nickles_fourth += 500
                        if count_nickles_fourth > nickles_fourth: 
                            count_nickles_fourth = nickles_fourth
                        print(count_nickles_fourth)
                    print(f"{nickles_fourth} in total")
                    
                    pennies_fourth = 24050
                    # ($240.50)
                    count_pennies_fourth = 0
                    print("Counting pennies...")
                    while count_pennies_fourth < pennies_fourth:
                        count_pennies_fourth += 2000
                        if count_pennies_fourth > pennies_fourth: 
                            count_pennies_fourth = pennies_fourth
                        print(count_pennies_fourth)
                    print(f"{pennies_fourth} in total")

                    print("The amount of coins presented to you have been counted :)")
                    time.sleep(2)
                    print("Are you going to be adding them up to get the total amount of dollars?")
                    time.sleep(4)

                    break
                else:
                    print("random_coin_code is not working")
            else:
                print("No, that is not one of the choices")
                time.sleep(.5)

        print("Now that you have finished with the coins")
        time.sleep(1)
        while True:
            enter_code_question_coins = input("Would you like to enter a code into the phone? [YES / NO] ").lower().strip()
            if enter_code_question_coins == "yes" or enter_code_question_coins == "y":
                while True:
                    code_in_phone_coins = input("Are you sure you want to enter a code into the phone? [YES / NO] ").lower().strip()
                    if code_in_phone_coins == "yes" or code_in_phone_coins == "y":
                        print("Okay if you're sure...")
                        clear_terminal()
                        while tries > 0:
                            enter_code_coins = input(f"Enter the code to escape, you have {tries} tries: ")
                            if enter_code_coins in codes or enter_code_coins in codes_bookshelf or enter_code_coins in carpet_codes or enter_code_coins in coins_codes:
                                print("The phone begins to ring and you pick it up, a light and airy voice speaks:")
                                time.sleep(2)
                                print("\"You have entered the correct code to escape, congratulations!\"")
                                time.sleep(4)
                                print("Confetti goes everywhere :)")
                                time.sleep(2)
                                clear_terminal()
                                print("GOOD JOB")
                                exit()
                            elif enter_code_coins in self_destruct_code_paper:
                                print("The phone begins to ring and you pick it up, a deep voice speaks:")
                                time.sleep(1)
                                print("\"You have entered the self destruct code, now initiating...\"")
                                time.sleep(1)
                                print("Three...")
                                time.sleep(1)
                                print("Two...")
                                time.sleep(1)
                                print("One...")
                                time.sleep(3)
                                clear_terminal()
                                print("You have failed the escape room,")
                                time.sleep(1)
                                print("and everything blows up")
                                exit()
                            else:
                                    tries -= 1
                                    print(f"You have {tries} left to input the code correctly")
                                    # end back to enter_code_coins
                                    if tries == 0:
                                        print("A deep voice answers the phone...")
                                        time.sleep(1)
                                        print("\"You have used all three tries to input the code correctly\"")
                                        time.sleep(2)
                                        print("\"You have FAILED!!\"")
                                        exit()
                    elif code_in_phone_coins == "no" or code_in_phone_coins == "n":
                        print("You step away from the phone")
                        break
                else:
                    print("No, answer is not one of the options")
                    # send back to code_in_phone_coins
            elif enter_code_question_coins == "no" or enter_code_question_coins == "n":
                print("You step away from the phone")
                break
            else:
                print("No, answer is not one of the options")
    elif choice == "carpet":
        if count_carpet == False:
            for i in range(1,51):
                print(i)
                time.sleep(0.2)
            print("You're starting to fall asleep...")
            time.sleep(3)
            clear_terminal()
            time.sleep(2)
            look_carpet = input("Do you want to look closer at the carpet? [YES / NO] ").strip().lower()
            if look_carpet == "yes" or look_carpet == "y":
                print("You kneel down and notice numbers stitched into the carpet in a different shade than the rest")
                time.sleep(2)
                random_carpet_code = random.choice(carpet_codes)
                time.sleep(2)
                print(random_carpet_code)
                time.sleep(4)
            else:
                print("You walk away from the carpet")
                time.sleep(2)
            print("Now that you have finished counting the carpet")
            time.sleep(1)
        else:
            print("You have already counted the carpet, I'm sure you're not actually that bored to do it again?")
            time.sleep(3)
        count_carpet = True
        clear_terminal()
        while True: 
            enter_code_question_carpet = input("Would you like to enter a code into the phone? [YES / NO] ").lower().strip()
            if enter_code_question_carpet == "yes" or enter_code_question_carpet == "y":
                while True: 
                    code_in_phone_carpet = input("Are you sure you want to enter a code into the phone? [YES / NO] ").lower().strip()
                    if code_in_phone_carpet == "yes" or code_in_phone_carpet == "y":
                        print("Okay if you're sure...")
                        clear_terminal()
                        while tries > 0:
                            enter_code_carpet = input(f"Enter the code to escape, you have {tries} tries: ")
                            if enter_code_carpet in codes or enter_code_carpet in codes_bookshelf or enter_code_carpet in carpet_codes or enter_code_carpet in coins_codes:
                                print("The phone begins to ring and you pick it up, a light and airy voice speaks:")
                                time.sleep(2)
                                print("\"You have entered the correct code to escape, congratulations!\"")
                                time.sleep(4)
                                print("Confetti goes everywhere :)")
                                time.sleep(2)
                                clear_terminal()
                                print("GOOD JOB")
                                exit()
                            elif enter_code_carpet in self_destruct_code_paper:
                                print("The phone begins to ring and you pick it up, a deep voice speaks:")
                                time.sleep(1)
                                print("\"You have entered the self destruct code, now initiating...\"")
                                time.sleep(1)
                                print("Three...")
                                time.sleep(1)
                                print("Two...")
                                time.sleep(1)
                                print("One...")
                                time.sleep(3)
                                clear_terminal()
                                print("You have failed the escape room,")
                                time.sleep(1)
                                print("and everything blows up")
                                exit()
                            else:
                                    tries -= 1
                                    print(f"You have {tries} left to input the code correctly")
                                    if tries == 0:
                                        print("A deep voice answers the phone...")
                                        time.sleep(1)
                                        print("\"You have used all three tries to input the code correctly\"")
                                        time.sleep(2)
                                        print("\"You have FAILED!!\"")
                                        exit()
                    elif code_in_phone_carpet == "no" or code_in_phone_carpet == "n":
                        print("You walk away from the phone")
                        break
                    else:
                        print("No, answer is not one of the options")
            elif enter_code_question_carpet == "no" or enter_code_question_carpet == "n":
                print("You walk away from the phone")
                break
            else:
                print("No, answer is not one of the options")
    elif choice == "bookshelf":
        print("You pick up one of the books titiled \"A Christmas Carol\"")
        time.sleep(1)
        read_cc = input("Would you like to read it? [YES / NO] ").strip().lower()
        if read_cc == "yes" or read_cc == "y":
            with open("christmas_carol.txt", "r") as book:
                print(book.read())
            while True:
                done_reading_cc = input("Are you done reading? [YES / NO] ").strip().lower()
                if done_reading_cc == "yes" or done_reading_cc == "y":
                    time.sleep(1)
                    clear_terminal()
                    print("OH NO!")
                    time.sleep(0.5)
                    print("The rest of the book has been ripped out! Only STAVE ONE remains!")
                    break
                elif done_reading_cc == "no" or done_reading_cc == "n":
                    print("Please, continue reading")
                else:
                    print("No, answer is not one of the options")

        elif read_cc == "no" or read_cc == "n":
            print("You walk away from the book")
            time.sleep(3)
        else:
            print("No, that is not one of the options")
        
        clear_terminal()

        print("Now that you have finished reading the book")
        time.sleep(1)
        enter_code_question_bookshelves = input("Would you like to enter a code into the phone? [YES / NO] ").lower().strip()
        if enter_code_question_bookshelves == "yes" or enter_code_question_bookshelves == "y":
            code_in_phone_bookshelves = input("Are you sure you want to enter a code into the phone? [YES / NO] ").lower().strip()
            if code_in_phone_bookshelves == "yes" or code_in_phone_bookshelves == "y":
                print("Okay if your sure...")
                clear_terminal()
                while tries > 0:
                    enter_code_bookshelves = input(f"Enter the code to escape, you have {tries} tries: ")
                    if enter_code_bookshelves in codes or enter_code_bookshelves in codes_bookshelf or enter_code_bookshelves in carpet_codes or enter_code_bookshelves in coins_codes:
                        print("The phone begins to ring and you pick it up, a light and airy voice speaks:")
                        time.sleep(2)
                        print("\"You have entered the correct code to escape, congratulations!\"")
                        time.sleep(4)
                        print("Confetti goes everywhere :)")
                        time.sleep(2)
                        clear_terminal()
                        print("GOOD JOB")
                        exit()
                    elif enter_code_bookshelves in self_destruct_code_paper:
                        print("The phone begins to ring and you pick it up, a deep voice speaks:")
                        time.sleep(1)
                        print("\"You have entered the self destruct code, now initiating...\"")
                        time.sleep(1)
                        print("Three...")
                        time.sleep(1)
                        print("Two...")
                        time.sleep(1)
                        print("One...")
                        time.sleep(3)
                        clear_terminal()
                        print("You have failed the escape room,")
                        time.sleep(1)
                        print("and everything blows up")
                        exit()
                    else:
                        tries -= 1
                        print(f"You have {tries} left to input the code correctly")
                        # end back to enter_code_bookshelves
                        if tries == 0:
                            print("A deep voice answers the phone...")
                            time.sleep(1)
                            print("\"You have used all three tries to input the code correctly\"")
                            time.sleep(2)
                            print("\"You have FAILED!!\"")
                            exit()
            elif code_in_phone_bookshelves == "no" or code_in_phone_bookshelves == "n":
                print("You move away from the phone")
            else:
                print("No, answer is not one of the options")
        elif enter_code_question_bookshelves == "no" or enter_code_question_bookshelves == "n":
            print("You move away from the phone")
        else:
            print("No, answer is not one of the options")
    elif choice == "paper":
        print("The papers are stained, you can barley make out the faint writing of some numbers")
        time.sleep(0.5)
        print("the numbers seem to be: 1001")
        enter_code_question_paper = input("Would you like to enter a code into the phone? [YES / NO] ").lower().strip()
        if enter_code_question_paper == "yes" or enter_code_question_paper == "y":
            code_in_phone_paper = input("Are you sure you want to enter a code into the phone? [YES / NO] ").lower().strip()
            if code_in_phone_paper == "yes" or code_in_phone_paper == "y":
                print("Okay if your sure...")
                clear_terminal()
                while tries > 0:
                    enter_code_paper = input(f"Enter the code to escape, you have {tries} tries: ")
                    if enter_code_paper in codes or enter_code_paper in codes_bookshelf or enter_code_paper in carpet_codes or enter_code_paper in coins_codes:
                        print("The phone begins to ring and you pick it up, a light and airy voice speaks:")
                        time.sleep(2)
                        print("\"You have entered the correct code to escape, congradulations!\"")
                        time.sleep(4)
                        print("Confetti goes everywhere :)")
                        time.sleep(2)
                        clear_terminal()
                        print("GOOD JOB")
                        exit()
                    elif enter_code_paper in self_destruct_code_paper:
                        print("The phone begins to ring and you pick it up, a deep voice speaks:")
                        time.sleep(1)
                        print("\"You have entered the self destruct code, now iniciating...\"")
                        time.sleep(1)
                        print("Three...")
                        time.sleep(1)
                        print("Two...")
                        time.sleep(1)
                        print("One...")
                        time.sleep(3)
                        clear_terminal()
                        print("You have failed the escape room,")
                        time.sleep(1)
                        print("and everything blows up")
                        exit()
                    else:
                        tries -= 1
                        print(f"You have {tries} left to input the code correctly")
                        # send back to enter_code_paper
                        if tries == 0:
                            print("A deep voice answers the phone...")
                            time.sleep(1)
                            print("\"You have used all three tries to input the code correctly\"")
                            time.sleep(2)
                            print("\"You have FAILED!!\"")
                            exit()
            elif code_in_phone_paper == "no" or code_in_phone_paper == "n":
                print("")
                # send back to choice
            else:
                print("No, answer is not one of the options")
                # send back to code_in_phone-paper
        elif enter_code_question_paper == "no" or enter_code_question_paper == "n":
            print("")
            # send back up to choice
        else:
            print("No, answer is not one of the options")
            # send back to enter-code_question_paper
    elif choice == "phone":
        while True: 
            enter_code_question = input("Would you like to enter a code into the phone? [YES / NO] ").lower().strip()
            if enter_code_question == "yes" or enter_code_question == "y":
                
                while True: 
                    code_in_phone = input("Are you sure you want to enter a code into the phone? [YES / NO] ").lower().strip()
                    if code_in_phone == "yes" or code_in_phone == "y":
                        print("Okay if you're sure...")
                        clear_terminal()
                        while tries > 0: 
                            enter_code = input(f"Enter the code to escape, you have {tries} tries: ").lower().strip()
                            if enter_code in codes or enter_code in codes_bookshelf or enter_code in carpet_codes or enter_code in coins_codes:
                                print("The phone begins to ring and you pick it up, a light and airy voice speaks:")
                                time.sleep(2)
                                print("\"You have entered the correct code to escape, congratulations!\"")
                                time.sleep(4)
                                print("Confetti goes everywhere :)")
                                time.sleep(2)
                                clear_terminal()
                                print("GOOD JOB")
                                exit()
                            elif enter_code in self_destruct_code_paper:
                                print("The phone begins to ring and you pick it up, a deep voice speaks:")
                                time.sleep(1)
                                print("\"You have entered the self destruct code, now initiating...\"")
                                time.sleep(1)
                                print("Three...")
                                time.sleep(1)
                                print("Two...")
                                time.sleep(1)
                                print("One...")
                                time.sleep(3)
                                clear_terminal()
                                print("You have failed the escape room,")
                                time.sleep(1)
                                print("and everything blows up")
                                exit()
                            else:
                                tries -= 1
                                print(f"You have {tries} left to input the code correctly")
                                if tries == 0:
                                    print("A deep voice answers the phone...")
                                    time.sleep(1)
                                    print("\"You have used all three tries to input the code correctly\"")
                                    time.sleep(2)
                                    print("\"You have FAILED!!\"")
                                    exit()
                                elif tries == 2:
                                    hint_frist = input("Do you want a hint? [YES / NO] ").lower().strip()
                                    if hint_frist == "yes" or hint_frist == "y":
                                        print("Check the papers!")
                                    elif hint_frist == "no" or hint_frist == "n":
                                        break
                                    else:
                                        print("No, answer is not one of the options")
                                elif tries == 1:
                                    hint = input("Do you want a hint? [YES / NO] ").lower().strip()
                                    if hint == "yes" or hint == "y":
                                        print("Check the book!")
                                    elif hint == "no" or hint == "n":
                                        break
                                    else:
                                        print("No, answer is not one of the options")
                                else:
                                    print("tries is not working")
                    elif code_in_phone == "no" or code_in_phone == "n":
                        print("You step away from the phone")
                    else:
                        print("No, answer is not one of the options")
            elif enter_code_question == "no" or enter_code_question == "n":
                print("You step away from the phone")
                break
            else:
                print("No, answer is not one of the options")
    else:
        print("You sit there within the room, pondering your existance before getting back up and deciding that you have to do something")
        # send back to choice