# AE | P1 | While Loops

# keeps running until a condition is met

import random
import time

goose = random.randint(1,20)
duck = 1 # <- start point

while goose > duck: # <- while is a key word to the while loop
    print("duck...")
    time.sleep(0.1)
    duck += 1 # <- incrementer (is used to change the iterator (used to keep track of the current of the ideratorn of the loop))

print("GOOSE!!")