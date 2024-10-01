def triangle (a , b , c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

print(triangle(3, 4, 5)) # True
print(triangle(3, 4, 7)) # False