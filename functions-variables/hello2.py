# ask user for their name
name = input("What's your name? ").strip().title()

# split user's name into first and last name

first_name, last_name = name.split(" ")

print(f"hello, {first_name} {last_name}")

