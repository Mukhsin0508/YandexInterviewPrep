# # Topic: Operators
# x = 4
# y = 4
# n = 7
# z = 5
# i = 9
# k = 9
#
# print(x==y) # true
# print(x!=y) # false
# print(n>z) # true
# print(i>=k) # true
# print(i<=n) # false
#
# # Topic: Logical Operators
# x = 5
# y = 8
# z = 12
# print(x<y and x == 5) # true
# print(z<y and x ==5) # false
# print(x<y or x ==5) # true
# print(not (x<y and x == 5)) # false
#
from calendar import month


# Identify the operands
# is not = ['is not']
# is = ['==', '!=', '>', '>=', '<=', 'and', 'or', 'not']

# name1 = "Geaoge"
# name2 = "Jack"
# name3 = name1
# print(name1 is name2)
# print(name2 is name3)
# print(name2 is not name3)
# print(name1 == name3)

# Membership Operators
# checks whether a value is present in a sequence or not
# in = ['in']
# not in = ['not in']

# text = "In the middle of difficulty lies opportunity" # Albert Einstein
# print("difficulty" in text) # True
# print("difficulty" not in text) # False
# print("ease" in text) # False
#
# for i in text:
#     print(i, end=' ')

# Control Structures
# if, elif, else
# used for decision-making, looping, and branching, etc

# Prompt the user to enter his age
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are an adult. You can participate in the election.")
# else:
#     print("You are not old enough, so you cannot participate in the election.")

# age = int(input("Enter your age: "))
#
# if 18 <= age <= 70:
#     print("You are an adult. You can participate in the election.")
# elif age <= 18:
#     print("You are not old enough, so you cannot participate in the election.")
# elif age >= 70:
#     print("You are too old to participate in the election.Time to Die!")
#

# 4, 18, 25, 65

# if age < 4:
#     print("It is free of charge for you!")
# elif 4 <= age <= 18:
#     print("You have to pay 5$")
# elif 18 <= age <= 65:
#     print("You have to pay 10$")
# else:
#     print("You have to pay 5$")

# Using multiple elif blocks
# if
# elif
# elif
# elif


# Testing Multiple Conditions
# requested_toppings = ["mushrooms", "extra cheese"]
# if "mushrooms" in requested_toppings:
#     print("Adding mushrooms.")
# if "pepperoni" in requested_toppings:
#     print("Adding pepperoni.")
# if "extra cheese" in requested_toppings:
#     print("Adding extra cheese.")
# print("\nFinished making your pizza!") # This way of writing the code is not efficient as it checks all the conditions
# even if the first condition is true. It is better to use if-elif-else statements to make the code more efficient.
# cuz when if-elif-else is used the code will stop checking the conditions once it finds the first true condition.
# This reduces the number of checks that need to be performed. And results in especially efficient code when the
# conditions are in a specific order.

# if-elif-else
# requested_toppings = ["mushrooms", "extra cheese"]
# if "mushrooms" in requested_toppings:
#     print("Adding mushrooms...")
# elif "pepperoni" in requested_toppings:
#     print("Adding pepperoni...")
# elif "extra cheese" in requested_toppings:
#     print("\n Adding extra cheese...")
# else:
#     print("Finished making your pizza!")

# # How to make the time-complexity of the code better
# requested_toppings = ["mushrooms", "extra cheese"]
# if "mushrooms" in requested_toppings:
#     print("\nAdding mushrooms...")
# if "pepperoni" in requested_toppings:
#     print("\nAdding pepperoni...")
# if "extra cheese" in requested_toppings:
#     print("\n Adding extra cheese...")
#     print("Finished making your pizza!")
#


# Match-case statement
# number either positive, negative or 0
# alien_color = ("green", "yellow", "red")

# number = int(input("Enter a number: "))
#
# if number > 0:
#     print("The number is positive")
# elif number < 0:
#     print("The number is negative")
# else:
#     print("The number is zero!")
#

#
# def hoursInMonth(month):
#
#     month1 = str(input("Enter 1st month: "))
#     month2 = str(input("Enter 2nd month: "))
#     month3 = str(input("Enter 3rd month: "))
#     month4 = str(input("Enter 4th month: "))
#     month5 = str(input("Enter 5th month: "))
#     month6 = str(input("Enter 6th month: "))
#
#     hours_in_a_month = 31 * 24
#
#     if month1 == month:
#         print(f"There are {hours_in_a_month} hours in {month1}")
#     elif month2 == month:
#         print(f"There are {hours_in_a_month} hours in {month2}")
#     elif month3 == month:
#         print(f"There are {hours_in_a_month} hours in {month3}")
#     elif month4 == month:
#         print(f"There are {hours_in_a_month} hours in {month4}")
#     elif month5 == month:
#         print(f"There are {hours_in_a_month} hours in {month5}")
#     elif month6 == month:
#         print(f"There are {hours_in_a_month} hours in {month6}")
#
#
#     total_hours = hours_in_a_month * 6
#     print(f"There are {total_hours} hours in {month1}, {month2}, {month3}, {month4}, {month5}, {month6}")
#
#
# hoursInMonth(month)


# number = int(input("Enter a number: "))
#
# if number % 2:
#     print("The number is odd")
# else:
#     print("The number is even")

# month_numbers = int(input("Enter a month number: "))
#
# hours_in_a_month = 31 * 24
#
# total_hours = month_numbers * hours_in_a_month
#
# print(total_hours)


# Vowels and Consonants
# vowel = ['a', 'e', 'i', 'o', 'u']
#
# letter = (input("Enter a letter: ")).lower()
#
# if letter in vowel:
#     print(f"{letter} is a vowel.")
# else:
#     print("The letter is a consonant.")
#


# create a dict
# bank_notes = {"$1":"George Washington",
#               "$2":"Thomas Jefferson",
#               "$5":"Abraham Lincoln",
#               "$10":"Alexander Hamilton",
#               "$20":"Andrew Jackson",
#               "$50":"Ulysses S. Grant",
#               "$100":"Benjamin Franklin"
#               }
#
# dollar = input("Enter a dollar bill: ")
#
# if dollar in bank_notes:
#     print(f"The person on the {dollar} bill is {bank_notes[dollar]}")
#


# user = input("Enter a square letter and a number: ").replace("", " ").split()
#
#
# if len(user) != 2:
#     print("Invalid input")
#     exit()
#
# letter = user[0].lower()
# number = int ( user[1] )
#
# if letter in "aceg":
#     if number % 2:
#         print("The square is black.")
#     else:
#         print("The square is white.")
# else:
#     print('you are on white square')


# How replace the position of a and b with each other's
# a = 8
# b = 10
#
# a, b = b, a
# print(a, b)


# i = 0
# while i < 5:
#     print(i, end=" ")
#     i += 1









