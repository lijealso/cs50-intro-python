'''
for _ in range(3): # [0, 1, 2]
    print("meow")

print("meow\n" * 3, end = '')
'''

while True:
    n = int(input("What's n: "))
    if n > 0:
        break

for _ in range(n):
    print("meow")

print("Thanks for meowing")