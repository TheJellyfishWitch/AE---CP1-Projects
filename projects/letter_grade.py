# AE | P1 | What is my Grade??

while True:
    try:
        grade = float(input("What is your grade in percentage [just a number, no extra characters]? "))
    except:
        print("That is not a number, try again")
    else:
        break

if grade >= 96.6:
    print(f"Your grade is {grade}% which is an A!")
elif grade >= 93.3:
    print(f"Your grade is {grade}% which is an A-")
elif grade >= 90.0:
    print(f"Your grade is {grade}% which is an B+")
elif grade >= 86.6:
    print(f"Your grade is {grade}% which is an B")
elif grade >= 83.3:
    print(f"Your grade is {grade}% which is an B-")
elif grade >= 80.0:
    print(f"Your grade is {grade}% which is an C+")
elif grade >= 76.6:
    print(f"Your grade is {grade}% which is an C")
elif grade >= 70.0:
    print(f"Your grade is {grade}% which is an D")
else:
    print(f"Your grade is {grade}% which is an F")
    print("Bro, what are you doing?")
