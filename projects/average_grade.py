# Addie Erickson | Average Grade

# 7 diff inputs
# output rouded to 2 decimals
# code works
# add loop

# stores grades
class_grades = {}


# counter to track # of classes
class_num = 1


while True:
    if class_num > 8:
        print("\nReached the maximum limit of 8 classes")
        break
    user_input = input(f"Enter grade for class {class_num} (when you are finished entering all classes put n/a): ").strip()

    if user_input.lower() == "done" or user_input.lower() == "n/a":
        if class_num = 1:
            print("No grades were entered.")
        break

class_grades[f"class_{class_num}"] = user_input
class_num += 1

# calculate
print("")