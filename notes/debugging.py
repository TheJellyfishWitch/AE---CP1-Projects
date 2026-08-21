# Addie Erickson | Debugging Notes

# Error types

# Syntax: you wrote it wrong, the computer will ususally tell you what is wrong
"""print("hello)"""
            # ^ you would need another quotation mark
  # indentation error
"""if True"""
"""print("this is true")""" # <- indentation error, no tab below, white space

# Logic:  you wrote it right but did the wrong steps
    #fixed by reading again, like acutally reading / explaining out loud
"""apples = 20"""
"""people = 3"""

"""print(apples * people)"""

# Run-time: happens when the code is running, sometimes or when the code is running and user is doing something
"""fav_num = input("what is your fav number?? ")"""
    # ^ string, not inetger so it cant add
"""print(4 + fav_num)"""
    # fixed, try / expect
while True: # <- if want to keep going can add a while true loop
    try:
        fav_num = int(input("what is tour fave number? "))
    except:
        print("thats not a number!!")
    else:
        break

print(4 + fav_num)