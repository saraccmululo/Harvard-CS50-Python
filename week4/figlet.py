from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fonts = figlet.getFonts()


def main():

    if len(sys.argv) == 1:
        # output text in a randon font
        random_font = random.choice(fonts)
        s = get_input("Input: ", random_font)
        print(s)

    elif len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font" and sys.argv[2] in fonts:
            s = get_input("Input: ", sys.argv[2])
            print(s)
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")


def get_input(prompt, f):
    text = input(prompt)
    figlet.setFont(font=f)
    return figlet.renderText(text)


main()
