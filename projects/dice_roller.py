# AE | Dice Roller

import random
import time

accpeted_dice = ["D4", "4", "D6", "6", "D8", "8", "D10", "10", "D12", "12", "D20", "20"]

while True:
    # get type of dice
    while True: 
        choice_of_dice = input("Which dice would you like to roll? [D4, D6, D8, D10, D12, D20]: ").upper().strip()
        if choice_of_dice in accpeted_dice:
            break
        else:
            print("That dice is not accepted, try again")

    # get number of dice
    while True: 
        try:
            number_of_dice = int(input(f"How many {choice_of_dice}(s) would you like to roll? "))
            if number_of_dice == 0:
                print("Enter a number greater than 0")
                continue
            elif number_of_dice < 0:
                print("Enter a positive number")
                continue
        except:
            print("That is not a number, try again")
        else:
            break

    # roll the dice
    if choice_of_dice == "D4" or choice_of_dice == "4":
        print(f"Rolling {number_of_dice} D4(s)...")
        time.sleep(1.5)
        for i in range(number_of_dice):
            print(f"Die #{i+1} rolled a {random.randint(1,4)}")
            time.sleep(1.5)
    elif choice_of_dice == "D6" or choice_of_dice == "6":
        print(f"Rolling {number_of_dice} D6(s)...")
        time.sleep(1.5)
        for i in range(number_of_dice):
            print(f"Die #{i+1} rolled a {random.randint(1,6)}")
            time.sleep(1.5)
    elif choice_of_dice == "D8" or choice_of_dice == "8":
        print(f"Rolling {number_of_dice} D8(s)...")
        time.sleep(1.5)
        for i in range(number_of_dice):
            print(f"Die #{i+1} rolled a {random.randint(1,8)}")
            time.sleep(1.5)
    elif choice_of_dice == "D10" or choice_of_dice == "10":
        print(f"Rolling {number_of_dice} D10(s)...")
        time.sleep(1.5)
        for i in range(number_of_dice):
            print(f"Die #{i+1} rolled a {random.randint(1,10)}")
            time.sleep(1.5)
    elif choice_of_dice == "D12" or choice_of_dice == "12":
        print(f"Rolling {number_of_dice} D12(s)...")
        time.sleep(1.5)
        for i in range(number_of_dice):
            print(f"Die #{i+1} rolled a {random.randint(1,12)}")
            time.sleep(1.5)
    elif choice_of_dice == "D20" or choice_of_dice == "20":
        print(f"Rolling {number_of_dice} D20(s)...")
        time.sleep(1.5)
        for i in range(number_of_dice):
            print(f"Die #{i+1} rolled a {random.randint(1,20)}")
            time.sleep(1.5)
    else:
        print("That is not a dice that is accepted, try again")

    time.sleep(1.5)

    again = input("Would you like to roll again? [yes / no] ").lower()
    if again == "no":
        print("Hope you had fun rolling! Goodbye now")
        break