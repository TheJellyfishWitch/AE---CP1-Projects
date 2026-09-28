# AE | P1 | User Sign In

import time

users = []

passes = []

# get username and pass
print("When prompted enter username and password for the system to memorize")
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
        break
    else:
        tries =+ 1
        remaining = max_tries - tries
        if remaining > 0:
            print(f"You have {remaining} tries left")
        else:
            print("You have no more tries :(")
            exit()

# sign in with info
print("Now that your information has been inputed, renter to signin")
username = input("Enter username: ")
usercheck = True if username in users else False
password = input("Enter password: ")
passcheck = True if password in passes else False

# check if invalid
if usercheck == False:
    print("Invalid username, try again")
elif passcheck == False:
    print("Invalid password, try again")
else:
    print("Successful log in, you are now signed in")

if usercheck and passcheck == True:
    print("Valid log in, signing in")

    # Sign in with info
print("Now that your information has been inputed, renter to signin")
username = input("Enter username: ")
password = input("Enter password: ")

# FIX 3: Verify that the password belongs to that specific user index
if username in users:
    user_index = users.index(username)
    if password == passes[user_index]:
        print("Successful log in, you are now signed in")
    else:
        print("Invalid password, try again")
else:
    print("Invalid username, try again")