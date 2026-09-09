# AE | Random Notes

import random # <- library module


ducks = random.randint(1,10) # <- lowest number, highest number. Information that we give the function to run. Includes last number
#              ^           ^  function, arguments, Return -> the info given back

print(f"There are {ducks} ducks!")


fruits = ["banana", "apple", "blueberry"]
ran_fruits = random.choice(fruits) # <- argument of a list, chooses one from the list
print(f"The fruit is...{ran_fruits}!")


pens = random.randrange(2,10,2) # <- start, stop (does not include when randomizing), step (even / odd)
#                     ^ it creates a list of numbers starting with the start point and stops before the stop, the step is which numbers are included within the list. then the computer chooses one of the numbers within the list [2,4,6,8]
print(f"There are {pens} pens")


chicken = random.randrange(1,15,3) # [1,3,6,9,12]
print(f"There are {chicken} chickens")


percent = random.random() # <- does not need arguments, randomizes a decimal, float between 0.0 & 1.0
# ^ if you don't tell the computer where to put the number it won't save it. its like thinking it in your head and then the person next to you knowing what you thought
print(f"You have a {percent:.2} grade")
#                          ^ add this to only have 2 decimal points. if decimal is 0.072, it will print all three because it does not register the '0'

