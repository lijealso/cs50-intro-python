import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def verify_beg(beg1):
    print(beg1)

def verify_end(end1):
    lista = []
    if end1 == '0':
        return False
    if end1.isalpha():
        return True
    for i in range(len(end1)):
        if end1[i].isdigit():
            lista.append(end1[i])
    if lista[0] == '0':
        return False

    if len(end1) > 1 and end1[-1].isalpha():
        for i in range(len(end1) - 1):
            if end1[i].isdigit():
                return False
    if len(end1) > 2 and end1[-1].isdigit() and end1[-2].isalpha() and end1[-3].isdigit():
        return False
    return True

def is_valid(s):
    length = len(s)
    for character in s:
        if character in string.punctuation or character == ' ':
            return False
    if (length < 2 or length > 6):
        return False
    if length == 2 and s[0].isalpha() and s[1].isalpha():
        return True
    if length > 2:
        end = s[2:len(s)]
        if verify_end(end) == False:
            return False
        else:
            return True

main()
