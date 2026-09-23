# AE | P1 | User Sign In

signin = input("Is this your first sign in [YES / NO]? ").lower().strip()

if signin == "yes":
    username = input("Enter first username: ")
    password = input("Enter first password: ")
else:
    username = input("Enter username: ")
    password = input("Enter password: ")