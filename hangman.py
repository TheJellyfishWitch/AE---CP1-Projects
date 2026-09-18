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


words = ["joe", "croquet", "cockpit", "bungler", "melancholy", "lollygag", "flabbergast", "paradiddle", "peekaboo", "fjord", "jazzy", "gipsy", "polka", "sphinx", "swivel", "quicky", "ribbed", "catawampus", "snickerdoodle", "gummy", "discombobulate", "bumfuzzle", "jock", "hocky", "phlegm", "jigsaw", "klutz", "rythms", "pharaoh", "crypts", "queue", "jinx", "zephyr", "memento", "quizzes", "vortex", "whisky", "lynx", "klutz", "glyph", "quaff"]

empty_hang = (
    "+---+\n"
        "|\n"
        "|\n"
        "|\n"
    "=========\n")

first_hang = (
    "+---+\n"
    " O  |\n"
    "    |\n"
    "    |\n"
    "=========\n")

second_hang = (
    "+---+\n"
    " O  |\n"
    " |  |\n"
    "    |\n"
    "=========\n")

third_hang = (
    "+---+\n"
    " O  |\n"
    "/|  |\n"
    "    |\n"
    "=========\n")

fourth_hang = (
    "+---+\n"
    " O  |\n"
    "/|\  |\n"
    "    |\n"
    "=========\n")

fifth_hang = (
    "+---+\n"
    " O  |\n"
    "/|\  |\n"
    "/   |\n"
    "=========\n")

fifth_hang = (
    "+---+\n"
    " O  |\n"
    "/|\  |\n"
    "/ \  |\n"
    "=========\n")

guessing_word = random.choice(words)
guessed_letters = []
incorrect = 0
lives = 6

if incorrect == "5":
    want_hint = input("Do you wnat a hint [YES / NO]? ").lower()
    if want_hint == "yes" or want_hint = "y":
        
while True:
    for word in words:
        print("What is your first letter? ")