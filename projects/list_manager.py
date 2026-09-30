# AE | P1 | Shopping List Manager

import time
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

user_items = []

clear_terminal()

while True:
    if not user_items:
        print("[]")
        print("Looks like there is nothing in your shopping list...")
        time.sleep(3)
        prompt = "What would you like to do to your shopping list? [ADD / EXIT] "
    else:
        prompt = "What would you like to do to your shopping list? [ADD / REMOVE / EXIT] "

    action = input(prompt).strip().lower()

    if action == "add":
        clear_terminal()
        print("You are now adding to your list")
        time.sleep(1.5)

        user_items.append(input("What would you like to add? "))

        shopping_list = "\n".join([f"-{item}" for item in user_items])
        clear_terminal()
        print(shopping_list)
        time.sleep(1.5)

    elif action == "remove" and user_items:
        clear_terminal()
        print("You are now removing items from your list")
        time.sleep(1.5)

        print(shopping_list)
        item_remove = input("What would you like to remove? ")
        
        if item_remove in user_items:
            user_items.remove(item_remove)
        else:
            print("Item not found in list")
            time.sleep(1.5)

        shopping_list = "\n".join([f"-{item}" for item in user_items])
        clear_terminal()
        print(shopping_list)
        time.sleep(1.5)

        if not user_items:
            print("[]")
            print("Looks like there is nothing in your shopping list...")
            time.sleep(3)

    elif action == "exit":
        clear_terminal()
        exit()

    else:
        clear_terminal()
        print(f"Invalid option: {action} not recognized. Please choose from the choices listed within the brackets")
        time.sleep(3)