# Parity Bits

bits = (input("Enter bits: "))

if len(bits) == 8:
    bits = [int(i) for i in bits]
    parity = bits.count(1)
    if parity % 2 == 0:
        print("Correct parity")
    else:
        print("Incorrect parity")
else:
    print("Enter 8 bits")

