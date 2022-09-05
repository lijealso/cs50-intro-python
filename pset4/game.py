import random
import sys

while True:
    try:
        level = int(input("Level: "))
        level >= 1
        rnd = random.randint(1, level)
    except (ValueError):
        pass
    else:
        while True:
            try:
                guess = int(input("Guess: "))
            except (ValueError):
                pass
            else:
                if guess < rnd:
                    print("Too small!")
                    pass
                elif guess > rnd:
                    print("Too large!")
                    pass
                else:
                    print("Just right!")
                    sys.exit()