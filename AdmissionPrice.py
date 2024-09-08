# Admission price for the group
age = (input("Enter your age: "))
total = 0

if age != 0:
    while len(age) != 0:
        try:
            age = int(age)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            total += 0

        if age <= 2:
            total += 0
        elif 3 <= age <= 12:
            total += 14
        elif 13 <= age <= 64:
            total += 23
        elif age >= 65:
            total +=18

        age = input("Enter your age: ").strip()
        if not age.isdigit():
            print("Enter digit")
            break

    print(f"The total admission price is ${total}")
else:
    print("You entered 0, no admission price to calculate.")
