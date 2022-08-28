expression = input("Expression: ").split(" ")

x = int(expression[0])
val = expression[1]
z = int(expression[2])

if val == "+":
    print(float(x + z))
elif val == "-":
    print(float(x - z))
elif val == "*":
    print(float(x * z))
elif val == "/":
    print(f'{(x / z):.1f}')
