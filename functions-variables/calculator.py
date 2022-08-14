x = float(input("Value of x: "))
y = float(input("Value of y: "))

z = round(x + y)
print(f"{z:,}")

z = x / y
print(z)
print(round(x / y, 2))

print(f"{z:.2f}")
