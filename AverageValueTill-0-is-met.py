number = int ( input ( "Please Enter bunch of numbers: " ) )


# Average value until 0 is met in loop
total = 0
count = 0

if number != 0:
    while number != 0:
        total += number
        count += 1
        number = int(input("Please Enter bunch of numbers: "))
    print(f"The average is {total / count}")

else:
    print("You entered 0, no average to calculate.")


