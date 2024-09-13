# Valid or no-valid password

password: str = input("Enter your password: ")

if len(password) >=8:

    if password.isalnum():
        print("Invalid password. Password must contain at least one special character")

    if password.isalpha():
        print("Invalid password. Password must contain at least one digit")

    if password.isupper():
        print("Invalid password. Password must contain at least one 'lowercase letter'")

    if password.islower():
        print("Invalid password. Password must contain at least one uppercase letter")

    if not (password.__contains__ ( "*" ) or password.__contains__ ( "&" )) \
                    or password.__contains__("#") or password.__contains__("@"):
        print("Invalid password. Password must contain at least one special character")

    else:
        print("Valid password: ", password)




