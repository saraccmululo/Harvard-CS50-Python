def main():
    user_input = input("Expression: ")
    x, y, z = user_input.split(" ")
    n1 = float(x)
    n2 = float(z)
    calculate(n1, n2, y)


def calculate(a, b, op):
    match op:
        case "+":
            print(f"{a+b:.1f}")
        case "-":
            print(f"{a-b:.1f}")
        case "/":
            print(f"{a/b:.1f}")
        case "*":
            print(f"{a*b:.1f}")


main()