answer = input("Greeting: ").strip().upper()

# Get First 5 character of a string in python
first_chars = answer[0:5]

if first_chars == "HELLO":
    print("$0")
elif first_chars[0] == "H":
    print("$20")
elif first_chars[0] != "H":
    print("$100")
