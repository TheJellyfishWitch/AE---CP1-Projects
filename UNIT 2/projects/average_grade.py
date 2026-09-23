# Addie Erickson | Average Grade

print("Hi, so I heard you wanna see what your average grade is? Cool, you only get 7 classes to put in. [put a 0 in the classes that you dont have]")

# take inputs and save as variables
# one
while True:
    try:
        grade_one = float(input("Enter grade for class one: "))
    except:
        print("thats not a number!!")
    else:
        break

# two
while True:
    try:
        grade_two = float(input("Enter grade for class two: "))
    except:
        print("thats not a number!!")
    else:
        break    

# three
while True:
    try:
        grade_three = float(input("Enter grade for class three: "))
    except:
        print("thats not a number!!")
    else:
        break

# four
while True:
    try:
        grade_four = float(input("Enter grade for class four: "))
    except:
        print("thats not a number!!")
    else:
        break

# five
while True:
    try:
        grade_five = float(input("Enter grade for class five: "))
    except:
        print("thats not a number!!")
    else:
        break

# six
while True:
    try:
        grade_six = float(input("Enter grade for class six: "))
    except:
        print("thats not a number!!")
    else:
        break

# seven
while True:
    try:
        grade_seven = float(input("Enter grade for class seven: "))
    except:
        print("thats not a number!!")
    else:
        break


average = (grade_one + grade_two + grade_three + grade_four + grade_six + grade_five + grade_seven) / 7


print(f"Your average grade is {average:.2f}!")