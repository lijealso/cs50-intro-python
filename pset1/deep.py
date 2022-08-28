answer = str(input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")).strip().capitalize().title().replace("-", " ")

match answer:
    case "42" | "Forty-two" | "Forty Two":
        print("Yes")
    case _:
        print("No")