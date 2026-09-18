# AE | P1 | Crew Shares

import random
import time

while True:
    try:
        number_pirates = int(input("How many pirate(s) are there? "))
        break
    except:
        print("That is not a number, try again")

number = 0

name_pirates = []

for i in range(number_pirates):
    name_pirates.append(input(f"What is the name of pirate #{i+1}? ").title())
    number += 1

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
for name in name_pirates:
    print(f"{name}'s share: {crew:.2f}")
    time.sleep(1.5)