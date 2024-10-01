def common_chars():
    J = input().strip()
    S = input().strip()

    count = 0

    for char in S:
        if char in J:
            count += 1
        else:
            continue

    print(count)

common_chars()
