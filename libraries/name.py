import sys

print("The name of this file is: %s" % sys.argv[0])


if len(sys.argv) < 2:
    sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")

for arg in sys.argv[1:]:
    print("My name is", arg)

# print("Hello, my name is %s" % sys.argv[1])