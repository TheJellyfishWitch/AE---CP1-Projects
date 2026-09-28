# AE | P1 | Shopping List Manager

import time

shopping_list = []

print(shopping_list)

if not shopping_list:
    print("Looks like there is nothing in your shopping list...")
    time.sleep(3)

while True:
    action = input("What would you like to do to your shopping list [ADD / REMOVE / EXIT]? ").lower().strip()

    if action == "add":
        print("You are now adding to your list")
        shopping_list.append(input("What would you like to add? "))
        print(shopping_list)
        time.sleep(1.5)
    elif action == "remove":
        print("You are now removing items from your list")
        shopping_list.append(input("What would you like to remove? "))
        print(shopping_list)
        time.sleep(1.5)
    elif action == "exit":
        exit()
    else:
        exit()