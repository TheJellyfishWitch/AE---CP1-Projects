# AE | P1 | User Sign In

import time

user = []

signin = input("Is this your first sign in [YES / NO]? ").lower().strip()

if signin == "yes":
    username = input("Enter username: ")
    password = input("Enter password: ")
else:
    username = input("Enter username: ")
    password = input("Enter password: ")

tries = 0