import random
import sys

def main():
    score = 10
    for _ in range(10):
        tries = 3
        level = get_level()
        x, y = generate_integer(level)
        while True:
            print(f"{x} + {y} = ", end = '')
            try:
                guess = int(input())
            except (ValueError):
                tries -= 1
                if tries == 0:
                    score -= 1
                    print(x + y)
                    break
            else:
                if guess == x + y:
                    break
                if guess != x + y:
                    print("EEE")
                    tries -= 1
                    if tries == 0:
                        score -= 1
                        print(x + y)
                        break
    print(score)
    sys.exit(0)

def get_level():
    while True:
        try:
            level = int(input('Level: '))
        except ValueError:
            pass
        else:
            if level in (1, 2, 3):
                break

    return level

def generate_integer(level):
    if level == 1:
        x = random.randrange(0, 9)
        y = random.randrange(0, 9)
        return x, y
    if level == 2:
        x = random.randrange(10, 99)
        y = random.randrange(10, 99)
        return x, y
    if level == 3:
        x = random.randrange(100, 999)
        y = random.randrange(100, 999)
        return x, y

if __name__ == "__main__":
    main()
