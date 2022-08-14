def main():
    x = input("What time is it? ")
    y = convert(x)

    if y >= 7 and y <= 8:
        print("breakfast time")
    elif y >= 12 and y <= 13:
        print("lunch time")
    elif y >= 18 and y <= 19:
        print("dinner time")


def convert(time):
    full_hour = time.split(":")
    hours = int(full_hour[0])
    minutes = int(full_hour[1])
    minutes_final = minutes / 60
    final = hours + minutes_final
    return final



if __name__ == "__main__":
    main()