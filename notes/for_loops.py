# AE | P1 | Loops Notes

import time

# Interaction
    # same thing to everything that is available

# plural
siblings = ["george", "jerry", "hehhe"]

# Idderator*
for sibling in siblings: # <- name of list
          # ^ 
    print(f"Good morning {sibling}!")

    # *common idderators: 1, x, or single verstion of list version


grades = [20, 88, 77, 67, 3, 75, 0, 100, 98]
average = 0

for grade in grades:
    average += grade
    print(f"{grade} was added")

average = average/len(grades)
print(f"The average grade is  {average:.2f}")

for i in range(20): # <- tells range when to stop, does not include, can also add 1 to make it not count 0, add 2 at end to count by "2s"
    print(i)

for i in range(20, 0, -1): # <- count backwards
    print(i)
    time.sleep(0.5)
    if i == 12:
        print("Wait its lunch time")
        break