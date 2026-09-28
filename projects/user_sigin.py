# AE | P1 | User Sign In

import time

users = []

passes = []

# get username and pass
print("When prompted enter username and password")
time.sleep(1.5)
users.append(input("Enter username: "))
passes.append(input("Enter password: "))

tries = 0
max_tries = 3

# renter pass word for confidentuality
while tries < max_tries:
    renter_pass = input("Renter password: ")

    # if it was incorrect, renter and then add 1 to tries
    if renter_pass == passes[0]:
        print("Password confirmed")
        time.sleep(1.5)
        break
    else:
        tries += 1
        remaining = max_tries - tries
        if remaining > 0:
            print(f"You have {remaining} tries left")
            time.sleep(1.5)
        else:
            print("Failed password identfication")
            exit()

# sign in with info
 
print("Now that your information has been inputed, renter to signin")
time.sleep(1.5)

while True:    
    username = input("Enter username: ")
    password = input("Enter password: ")

    # check if username is inputed correctly for signin
    if username in users:
        user_index = users.index(username)
        if password == passes[user_index]:
            print("Successful log in, you are now signed in")
            time.sleep(1.5)
            break
        else:
            print("Invalid password, try again")
            time.sleep(1.5)
    else:
        print("Invalid username, try again")
        time.sleep(1.5)