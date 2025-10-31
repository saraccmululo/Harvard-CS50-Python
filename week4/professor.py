import random


def main():
    level = get_level()
    print(level)
    score = 0
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        result = x+y
        counter = 0
        while counter < 3:
            user_input = input(f"{x} + {y} = ")
            answer = int(user_input)
            if answer != result:
                print("EEE")
                counter += 1
            else:
                score += 1
                break
        if counter == 3:
            print(f"{x} + {y} = ",result)
    print(f"Score: {score}")


def get_level():
    while True:
        level = input("Level: ")
        if level in "1,2,3":
            n = int(level)
            return n


def generate_integer(level):
    if level not in [1, 2, 3]:
        raise ValueError("Make sure level is 1 or 2 or 3.")
    else:
        if level == 1:
            return random.randint(0, 9)
        if level == 2:
            return random.randint(10, 99)
        if level == 3:
            return random.randint(100, 999)


if __name__ == "__main__":
    main()
