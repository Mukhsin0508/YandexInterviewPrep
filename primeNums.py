# print prime numbers, prime numbers are numbers that are only divisible by 1 and themselves
list = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

for i in list:
    if i > 1:
        for j in range(2, i): # j is the divisor, i is the dividend, e.g: (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8)

            if i % j == 0:
                break
        else:
            print(i, end=" ")