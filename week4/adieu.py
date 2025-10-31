import inflect

p = inflect.engine()


def main():
    names = []
    while True:
        try:
            name = input()
            names.append(name)
        except EOFError:
            print(f"Adieu, adieu, to {p.join(names)}")
            break

main()
