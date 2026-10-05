# AE | P1 | Multilication Table

import time
import os

def clear_terminal(): # clears the terminal
    os.system('cls' if os.name == 'nt' else 'clear')

# use a loop
# output is a table, use list and then do for row and num
    # x   | 1 |   2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
    # -------------------------------------------------------
    #  1 ||  1 |  2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
    #  2 ||  2 |  4 |etc.
    #  3 ||  3 |  6 |etc.
    #  4 ||  4 |  8 |etc.
    #  5 ||  5 | 10 |etc.
    #  6 ||  6 | 12 |etc.
    #  7 ||  7 | 14 |etc.
    #  8 ||  8 | 16 | etc.
    #  9 ||  9 | 18 | etc.
    # 10 || 10 | 20 |etc.
    # 11 || 11 | 22 | etc.
    # 12 || 12 | 24 | etc.

print("Here is a times table up too 12 :)")

time.sleep(2.5)

# 12 times table
print("  x" + " |", end="") # header
for col in range(1,13):
    print(f"{col:4}", end="")
print()

print("-" * 55)

for row in range(1,13):
    print(f"{row:3} |", end="")

    for col in range(1,13):
        product = row * col
        print(f"{product:4}", end="")
    print()

while True: 
    time.sleep(1.5)
    while True:
        more = input("Do you want a times table with more? It can go up too 15! [YES / NO] ").strip().lower()
        if more == "yes" or more == "y":
            clear_terminal()
            break
        elif more == "no" or more == "n":
            print("Hope you had fun!")
            exit()
        else:
            print("That input is not accepted, try again")
            time.sleep(1.5)

    how_long = int(input("How much more? [13, 14, 15] "))

    if how_long == 13:
        clear_terminal()
        print("Here is your desired output: ")
        time.sleep(1.5)
        # 13 times table
        print("  x" + " |", end="") # header
        for col in range(1,14):
            print(f"{col:4}", end="")
        print()

        print("-" * 59)

        for row in range(1,14):
            print(f"{row:3} |", end="")

            for col in range(1,14):
                product = row * col
                print(f"{product:4}", end="")
            print()


    elif how_long == 14:
        clear_terminal()
        print("Here is your desired output: ")
        time.sleep(1.5)
        
        # 14 times table
        print("  x" + " |", end="") # header
        for col in range(1,15):
            print(f"{col:4}", end="")
        print()

        print("-" * 63)

        for row in range(1,15):
            print(f"{row:3} |", end="")

            for col in range(1,15):
                product = row * col
                print(f"{product:4}", end="")
            print()

    elif how_long == 15:
        clear_terminal()
        print("Here is your desired output: ")
        time.sleep(1.5)
        
        # 15 times table
        print("  x" + " |", end="") # header
        for col in range(1,16):
            print(f"{col:4}", end="")
        print()

        print("-" * 67)

        for row in range(1,16):
            print(f"{row:3} |", end="")

            for col in range(1,16):
                product = row * col
                print(f"{product:4}", end="")
            print()

    else:
        print("That input is not accepted, please try again")
        continue