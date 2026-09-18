# AE | P1 | Crew Shares

import random
import time

name_pirates = []

while True:
    try:
        number_pirates = int(input("How many pirates are there? "))
    except:
        print("That is not a number, try again")
    else:
        break

number = 0

while True:
    if number_pirates >= number:
        for i in range(number_pirates):
            name_pirates = input(f"What is the name of pirate #{i+1}? ")
        number += 1
    else:
        break

number_pirates_w_other = number_pirates + 2 

units = random.randint(500, 5000)

yondu = units * 0.13
peter = yondu * 0.11
crew = peter / number_pirates

print(f"Number of crew: {number_pirates}")
time.sleep(1.5)
print(f"Number of total pirates: {number_pirates_w_other}")
time.sleep(1.5)
print(f"Units found: {units:.2f}")
time.sleep(1.5)
print(f"Yondu's share: {yondu:.2f}")
time.sleep(1.5)
print(f"Peter's share: {peter:.2f}")
time.sleep(1.5)
print(f"Crew's share: {crew:.2f}")
time.sleep(1.5)