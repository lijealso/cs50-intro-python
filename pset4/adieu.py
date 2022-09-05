import sys
lista = []

while True:
    try:
        a = input("Name: ")
    except EOFError:
        print("Adieu, adieu, to ", end = '')
        if len(lista) == 1:
            print(lista[0])
            sys.exit()
        if len(lista) == 2:
            print(lista[0] + " and " + lista[1])
            sys.exit()
        while len(lista) > 2:
            print(lista[0] + ', ', end='')
            lista.remove(lista[0])
        print(lista[-2] + ", and " + lista[-1])
        sys.exit()
    else:
        lista.append(a)