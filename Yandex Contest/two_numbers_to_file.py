def sum_two_numbers():

    with open('input.txt', 'r') as infile:

        a, b = map(int, infile.readline().split())


    with open('output.txt', 'w') as outfile:

        outfile.write(str(a+b) + '\n')

sum_two_numbers()