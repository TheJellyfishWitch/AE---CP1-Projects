# AE | P1 | Hangman

import random
import time

# LIST words to use
# DISPLAY empty handman
# WHILE TRUE
    # GET letter from user
    # DISPLAY if the letter is in / isn't in the word
    # CHECK if letter is all the way spelled out
    # CHECK if hangman is dead
    # IF hint is inputed by user
        # DISPLAY number of letters in word
# GET if user want to play again


words = ["joe", "croquet", "cockpit", "bungler", "melancholy", "lollygag", "flabbergast", "paradiddle", "peekaboo", "fjord", "jazzy", "gipsy", "polka", "sphinx", "swivel", "quicky", "ribbed", "catawampus", "snickerdoodle", "gummy", "discombobulate", "bumfuzzle", "jock", "hocky", "phlegm", "jigsaw", "klutz", "rythms", "pharaoh", "crypts", "queue", "jinx", "zephyr", "memento", "quizzes", "vortex", "whisky", "lynx", "klutz", "glyph", "quaff", "word"]
stages = [
    r"""+---+
    |
    |
    |
=========""",
    r"""+---+
 O  |
    |
    |
=========""",
    r"""+---+
 O  |
 |  |
    |
=========""",
    r"""+---+
 O  |
/|  |
    |
=========""",
    r"""+---+
 O  |
/|\ |
    |
=========""",
    r"""+---+
 O  |
/|\ |
/   |
=========""",
    r"""+---+
 O  |
/|\ |
/ \ |
========="""]

while True: 
    guessing_word = random.choice(words)
    guessed_letters = []
    incorrect = 0
    lives = 6

    while True:
        print(stages[incorrect])

        display_word = ""
        for letter in guessing_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print(f"Word: {display_word}\n")

        guess = input("Guess a letter: ").lower().strip()

        if guess in guessed_letters:
            print(f"You already guesses the letter {guess}, try again")
            time.sleep(1.5)
            continue

        if guess in guessing_word:
            print("Correct")
            time.sleep(1.5)
            if guess not in guessed_letters:
                guessed_letters.append(guess)
        else:
            print("Incorrect, try again")
            time.sleep(1.5)
            incorrect += 1
            lives -= 1

        

        player_won = True
        for letter in guessing_word:
            if letter not in guessed_letters:
                player_won = False

        if player_won:
            print(f"You win! The word was: {guessing_word}")
            break

        if lives <= 0:
            print(stages[incorrect])
            print(f"Game over! The word was {guessing_word}")
            break

        if incorrect == 5:
                    want_hint = input("Do you wnat a hint [YES / NO]? ").lower()
                    if want_hint == "yes" or want_hint == "y":
                        print(f"Hint: the word has {len(guessing_word)} letters")
                        time.sleep(1.5)
        
    again = input("Would you like to play again [YES / NO]? ")
    if again == "no" or again == "n":
        break