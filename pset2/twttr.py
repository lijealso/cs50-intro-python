sentence = input("Input: ")
vowels = "aAeEiIoOuU"
output = ""

for letter in sentence:
    if letter not in vowels:
        output += letter

print("Output:", output)
