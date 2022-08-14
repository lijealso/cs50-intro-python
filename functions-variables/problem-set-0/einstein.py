import math

def calculate_energy(mass):
    c = 300000000
    energy = format(mass * math.pow(c, 2), '.0f')
    return energy


def main():
    mass = int(input("m: "))
    print("E: " + str(calculate_energy(mass)))

main()