# Addie Erickson | Madlib

import time

print("Title: Space Shuttle")
time.sleep(2)

# madlib inputs
country = input("Enter a country: ").capitalize()
noun = input("Enter a noun: ").lower()
name = input("Enter a name: ").capitalize()
plural_noun = input("Enter a plural noun: ").lower()
verb_ing = input("Enter a verb ending in \"ing\": ").lower()
city = input("Enter a city: ").capitalize()
plural_noun_two = input("Enter a plural noun: ").lower()
adjective = input("Enter a adjective: ").lower()
noun_two = input("Enter a noun: ").lower()
# make sure number is a number
while True:
    try:
        number = int(input("Enter a number: "))
    except:
        print("thats not a number!!")
    else:
        break
while True:
    try:
        number_two = int(input("Enter a number: "))
    except:
        print("thats not a number!!")
    else:
        break

noun_three = input("Enter a noun: ").lower()
planet = input("Enter a planet: ").capitalize()
adjective_two = input("Enter a adjective: ").lower()
verb = input("Enter a verb: ").lower()
verb_two = input("Enter a verb: ").lower()
verb_ing_two = input("Enter a verb ending in \"ing\": ").lower()
adverb = input("Enter a adverb: ").lower()
adjective_three = input("Enter a adjective: ").lower()
plural_noun_three = input("Enter a plural noun: ").lower()
verb_three = input("Enter a verb: ").lower()

# madlib outputs
print(f"In 2026 the {country} launched the first real space {noun}. It was named {name} and was piloted by two brave {plural_noun}.")
time.sleep(4)
print(f"They had practiced {verb_ing} for two years and were expert {plural_noun_three}. {name} took off from {city} using its powerful {plural_noun_two} and soared off into the {adjective} blue {noun_two}.")
time.sleep(6)
print(f"For those watching from {planet} it was a/an {adjective_three} sight to {verb_two}! Who could really {verb_three} that there were two {plural_noun} in space? It was mind {verb_ing_two}.")
time.sleep(8)
print(f"After {number_two} orbits the shittle landed {adverb} back on {planet}, it was a/an {adjective_three} day for the {country} space program.")
time.sleep(6)
print("Thank you for doing my madlib :)")