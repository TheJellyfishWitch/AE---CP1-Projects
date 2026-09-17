# AE | P1 | Debug with the Debugger

# Ravager Snack Bar
import random

pirate_name = input("What's your name, pirate? ")
snack_name = input("What snack do you want? ")

price = random.randint(2, 8)  # random price in credits
quantity = int(input("How many would you like? ")) # CHANGED | made quantity a integer so it could have stuff done to it by other numbers

total = price * quantity

discounted_total = total - (total * 0.10) # REMOVED | got rid of the '- 2' becuase we just wanna give them a 10% discount

tax_rate = 0.08
total_with_tax = discounted_total + (discounted_total * tax_rate)

print("Hello, " + pirate_name + "! Here's your order summary:")
print("Snack: " + snack_name) # REMOVED & ADDED | wrong variable name, has a capital not a underscore
print("Price per snack: " + str(price) + " credits")
print("Total before tax: " + str(total)) # CHANGED | total before tax not the price
print("Total with tax: " + str(round(total_with_tax, 2)) + " credits") # ADDED | parentheses