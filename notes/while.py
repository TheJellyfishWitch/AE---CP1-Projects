# AE | P1 | While Loops

# keeps running until a condition is met

import random
import time

goose = random.randint(1,50)
duck = 1 # <- start point

while goose > duck: # <- while is a key word to the while loop, goose > duck is the end point
    print("duck...")
    time.sleep(0.1)
    duck += 1 # <- incrementer (is used to change the iterator (used to keep track of the current of the ideratorn of the loop))
    if duck == 15:
        print("Game over")
        break
else: # <- only if the contidtion becomes false, if you do a break it will not run
    print("GOOSE!!")

count = 1

while count < -30:
    print(count)
    time.sleep(0.1)
    count -= 1

number = random.randint(1,101)

tries = 1

while True:
    while True:
        try:
            guess = int(input("Guess a number between 1 - 100, you have 5 tries: "))
            if guess < 0 or guess > 100: # <- I got 67 once
                print("No, go read the instructions again")
                time.sleep(.5)
                continue # <- starts the next iteration
            break # <- exits the loop it is inside of
        except:
            print("No, you cannot do that")
            time.sleep(.5)
    if tries == 5:
        print("You ran out of tries to guess, womp, womp")
        time.sleep(.5)
        break

    if guess == number:
        print("You win!")
        break
    elif guess < number:
        print("That number is to low")
        time.sleep(.5)
        tries += 1
    elif guess > number:
        print("That number is too high")
        time.sleep(.5)
        tries += 1
    else:
        print("That number is not correct and also how did you get here?")
        time.sleep(.5)
        tries += 1