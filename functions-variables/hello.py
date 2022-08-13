# Ask user for their name
# remove whitespace from string
# capitalize user's name
# not only first word
name = input("What's you name? ").strip().capitalize().title()

# Say hello to user
print("hello, " + name)
print("hello", name)

# separator
print("hello,", name, sep="???")

# default end value is \n
print("hello, ", end='')
print(name)

# quotes inside print statements
print('hello, "friend"')
print("hello, \"friend\"")

# just playing
print("hello,", name, sep='-', end='\t')

# f string
print(f"hello, {name}")