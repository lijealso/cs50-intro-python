import math

def main():
    x = int(input("Value of x = "))
    print("x squared = ", square(x))

def square(n):
    return int(math.pow(n, 2))

main()