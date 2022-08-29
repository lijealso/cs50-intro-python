import random

coin = random.choice(["heads", "tails"])
print(coin)

integer = random.randint(1,2)
print(integer)

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)