# AE | P1 | Factorial Calculator

import math

# Pseudocode
    # GET user input of what number ot factorial
    # FOR every number in list of inputed numbers factor it
    # OUTPUT numbers before being outputed
    # OUPUT numbers after being outputed

# sample
    # What number do you want the factorial of: 5
    # 5 × 4 × 3 × 2 × 1 = 120
    # What number do you want the factorial of: 0
    # 0 = 1

numbers = []

numbers_factored = []

while True:
    try:
        numbers.append(int(input("What number would you like to factor? ")))
    except:
        print("That is not a number accepted, try again")
    else:
        break

while True:
    another_number = input("Would you like to factor another number? [YES / NO] ").strip().lower()

    if another_number == "yes" or another_number == "y":
        while True:
            try:
                numbers.append(int(input("What number would you like to factor? ")))
            except:
                print("That is not a number accepted, try again")
            else:
                break
    else:
        break

for i in numbers:
    numbers_factored.append((math.factorial(i)))

print(f"Here are your number(s) before being factored: {numbers}")

print(f"Here are your number(s) after being factored: {numbers_factored}")