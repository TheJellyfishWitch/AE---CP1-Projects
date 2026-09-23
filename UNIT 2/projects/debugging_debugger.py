# AE | P1 | Debug with the Debugger

# Ravager Snack Bar
import random
import time

in_stock_snacks = ["cheese", "goat cheese", "pickles", "pirates booty", "chocolate gold coins"]

pirate_name = input("What's your name, pirate? ").title()

print("In stock we have cheese, goat cheese, pickles, pirates booty, and chocolate gold coins.")
snack_name = input("What snack do you want? ").capitalize()

price = random.randint(2, 8)  # random price in credits

while True: 
    while True:
        try:
            quantity = int(input("How many would you like? ")) # CHANGED | made quantity a integer so it could have stuff done to it by other numbers
        except:
            print("That is not a number try again")
        else:
            break

    total = price * quantity

    if total >= 20:
        print("Because your total is above / equal too 20 credits, you get a loyalty bonus!")
        total - 1
        time.sleep(2)
        break
    else:
        more = input(f"Would you like to get more {snack_name} to get a loyalty bonus [YES / NO]? ").lower()
        if more == "no" or more == "nah" or more == "nope":
            print("Fine")
            time.sleep(1)
            break
        else:
            continue


discounted_total = total - (total * 0.10) # REMOVED | got rid of the '- 2' becuase we just wanna give them a 10% discount

tax_rate = 0.08
total_with_tax = discounted_total + (discounted_total * tax_rate)

print("Hello, " + pirate_name + "! Here's your order summary:")
time.sleep(2)
print("Snack: " + snack_name) # REMOVED & ADDED | wrong variable name, has a capital not a underscore
time.sleep(2)
print("Price per snack: " + str(price) + " credits")
time.sleep(2)
print("Total before tax: " + str(total)) # CHANGED | total before tax not the price
time.sleep(2)
print("Total with tax: " + str(round(total_with_tax, 2)) + " credits") # ADDED | parentheses
time.sleep(2)