# AE | Dice Roller

import random

while True: 
    try:
        choice = input("Which dice would you like to roll? [D4. D6, D8, D10, D12, D20]: ").upper()
        if choice == "D4":
            d_four = random.randint(1,4)
            print(f"You rolled a {d_four}!")
        elif choice == "D6":
            d_six = random.randint(1,6)
            print(f"You rolled a {d_six}!")
        elif choice == "D8":
            d_eight = random.randint(1,8)
            print(f"You rolled a {d_eight}!")
        elif choice == "D10":
            d_ten = random.randint(1,10)
            print(f"You rolled a {d_ten}!")
        elif choice == "D12":
            d_twelve = random.randint(1,12)
            print(f"You rolled a {d_twelve}!")
        elif choice == "D20":
            d_twenty = random.randint(1,20)
            print(f"You rolled a {d_twenty}!")
        else:
            print("That is not a dice that is accepted, try again")
    except:
        print("an uxexpected error as occurred, try again")
    else:
        break