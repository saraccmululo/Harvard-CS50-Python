def main():
    x = get_fract("Fraction: ")
    if x == "E" or x == "F":
        print(x)
    else:
        print(f"{x}%")


def get_fract(prompt):
    while True:
        try:
            user_input = input(prompt)
            s = user_input.split("/")
            if "/" not in user_input:
                continue
            s1, s2 = s[0], s[1]
            x = int(s1)
            y = int(s2)
            if x > y or x<0 or y <= 0:
                continue
            percent = (x/y) * 100
            if percent <= 1:
                return "E"
            if percent >= 99:
                return "F"
            return f"{percent:.0f}"  # to remove the decimal and round the number
        except (ValueError, ZeroDivisionError):
            continue


main()
