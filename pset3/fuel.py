def main():
    s = get_fuel("What's X/Y: ")
    print(s)

def get_fuel(prompt):
    while True:
        try:
            inp = input(prompt).split("/")
            X = int(inp[0])
            Y = int(inp[1])
            div = X / Y
        except (ValueError, ZeroDivisionError):
            pass
        else:
            if (X > Y):
                pass
            elif (X / Y * 100) <= 1:
                return "E"
            elif (X / Y * 100) >= 99:
                return "F"
            else:
                return str(round(div * 100)) + "%"
                
main()