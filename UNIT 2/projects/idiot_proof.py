# AE | Idiot Proof

# inputs
name = input("Enter full name: ").title()

while True:
    try:
        gpa = float(input("Enter GPA: "))

        if gpa < 0.0 or gpa > 4.5:
            raise
    except:
        print("not a valid GPA, try again")
    else:
        break

while True:
        input_phone_number = input("Enter phone number [must be 10 digits long]: ")

        if input_phone_number.isdigit() and len(input_phone_number) == 10:
            break
        else:
            print("not a valid phone number, try again")

# format phone number
phone_number = f"{input_phone_number[0:3]} {input_phone_number[3:6]} {input_phone_number[6:]}"


# outputs
print("\n---Summary---")
print("Name:", name)
print("Phone Number:", phone_number)
print(f"GPA: {gpa:.1f}")