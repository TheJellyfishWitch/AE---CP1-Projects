# AE | P1 | Tic Tac Toe

available_spaces = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]

empty_board = (
"   |   |   \n"
"-----------\n"
"   |   |   \n"
"-----------\n"
"   |   |   \n")
print(empty_board)

# player names
player_one = input("Player One, what is your name? ").title()
player_two = input("Player Two, what is your name? ").title()

player_one_space = input(f"{player_one}, where would you like to go? [A1, A2, A3, etc.] ").upper()

if player_one_space == "A1":
    print(
    " x |   |   \n"
    "-----------\n"
    "   |   |   \n"
    "-----------\n"
    "   |   |   \n")
elif player_one_space == "A2":
    print(
    "   | x |   \n"
    "-----------\n"
    "   |   |   \n"
    "-----------\n"
    "   |   |   \n")
elif player_one_space == "A3":
    print(
    "   | x |   \n"
    "-----------\n"
    "   |   |   \n"
    "-----------\n"
    "   |   |   \n")
elif player_one_space == "B1":
    print(
    "   | x |   \n"
    "-----------\n"
    "   |   |   \n"
    "-----------\n"
    "   |   |   \n")
elif player_one_space == "B2":
    print(
    "   | x |   \n"
    "-----------\n"
    "   |   |   \n"
    "-----------\n"
    "   |   |   \n")
elif player_one_space == "B3":
    print(
    "   | x |   \n"
    "-----------\n"
    "   |   |   \n"
    "-----------\n"
    "   |   |   \n")
elif player_one_space == "C1":
    print(
    "   | x |   \n"
    "-----------\n"
    "   |   |   \n"
    "-----------\n"
    "   |   |   \n")
elif player_one_space == "C2":
    print(
    "   | x |   \n"
    "-----------\n"
    "   |   |   \n"
    "-----------\n"
    "   |   |   \n")
elif player_one_space == "C3":
    print(
    "   |   |   \n"
    "-----------\n"
    "   |   |   \n"
    "-----------\n"
    "   |   | x \n")