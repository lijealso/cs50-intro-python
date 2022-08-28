inserted = 0
total = 0

while True:
    inserted = int(input("Insert coin: "))
    if inserted == 5 or inserted == 10 or inserted == 25:
        total += inserted
        if total >= 50:
            print("Change owed:", total - 50)
            break
        else:
            print("Amount due:", 50 - total)
    else:
        print("Amount due:", 50 - total)




