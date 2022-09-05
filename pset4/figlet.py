from pyfiglet import Figlet
import random
import sys

arguments = ["-f", "--font"]

figlet = Figlet()

fonts = figlet.getFonts()
tam_fonts = len(fonts) # 425

if len(sys.argv) == 1:
    font_choice = random.choice(fonts)
    figlet.setFont(font = font_choice)
    sentence = input("Input: ")
    print(figlet.renderText(sentence))
elif len(sys.argv) != 3 or sys.argv[1] not in arguments or sys.argv[2] not in fonts:
    sys.exit("Invalid usage")
else:
    figlet.setFont(font = sys.argv[2])
    sentence = input("Input: ")
    print(figlet.renderText(sentence))