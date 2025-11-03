def main():
    while True:
        user_input = input("Fraction: ").strip()
        if "/" in user_input:
            try:
                n = convert(user_input)
            except(ValueError, ZeroDivisionError):
                continue
            gauge(n)
            print(x)#print(f"{n:.0f}%")# to remove the decimal and round the number
            break

def convert(fraction):
    s = fraction.split("/")
    if len(s) !=2:
        raise ValueError
    s1, s2 = s[0], s[1]
    try:
        x = int(s1)
        y = int(s2)
    except ValueError:
        raise ValueError
    if x > y or x<0:
        raise ValueError
    if y == 0:
        raise ZeroDivisionError

    percent = round((x/y) * 100)
    return percent


def gauge(percentage):
    if percentage <= 1:
        return "E"
    if percentage >= 99:
        return "F"

    return f"{percentage}%"


if __name__ == "__main__":
    main()
