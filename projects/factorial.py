# AE | P1 | Factorial Calculator

import math

# Pseudocode
    # GET user input of what number ot factorial
    # FOR every number in list of inputed numbers factor it
    # OUTPUT numbers before being outputed
    # OUPUT numbers after being outputed

# sample
    # What number do you want the factorial of: 5
    # 5 × 4 × 3 × 2 × 1 = 120 (how a factor works)
    # OUTPUT [numbers wanted to factor]
    # OUTPUT [numbers factored]
    # What number do you want the factorial of: 0
    # OUTPUT [0]
    # OUTPUT [1]

numbers = []

while True:
    try:
        number_input = int(input("What number would you like to factor? "))
        if number_input >= 0:
            numbers.append(number_input)
            break
        else:
            print("That is not a number accepted, try again")
    except:
        print("That is not a number accepted, try again")
    else:
        break



while True:
    another_number = input("Would you like to factor another number? [YES / NO] ").strip().lower()

    if another_number == "yes" or another_number == "y":
        while True:
            try:
                number_input = int(input("What number would you like to factor? "))
                if number_input >= 0:
                    numbers.append(number_input)
                    break
                else:
                    print("That is not a number accepted, try again")
            except:
                print("That is not a number accepted, try again")
            else:
                break
    else:
        break

numbers_factored = list(map(math.factorial, numbers))

print(f"Here are your number(s) before being factored: {numbers}")

print(f"Here are your number(s) after being factored: {numbers_factored}")