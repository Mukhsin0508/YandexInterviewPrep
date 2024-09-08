# # CaesarCipher
#
# def caesarCipher(text, shift):
#     result = ""
#     for i in range(len(text)):
#         char = text[i]
#         if char.isupper():
#             result += chr((ord(char) + shift - 65) % 28 + 65) # 65 is the ASCII value of 'A'
#         elif char.islower():
#             result += chr((ord(char) + shift - 97) % 28 +97) # 97 is the ASCII value of 'a'
#         else:
#             result += char
#     print(result)
# caesarCipher(input("Enter text: "), int(input("Enter shift: ")))