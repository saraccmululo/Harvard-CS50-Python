import random

def main():
    result = None
    while True:
        level = input("Level: ")
        if level.isdigit():
            n = int(level)
            if n > 0:
                result = random.randint(1, n)
                break

    while True:
        user_input = input("Guess: ")
        if user_input.isdigit():
            guess = int(user_input)
            if guess > 0:
                if guess > result:
                    print("Too large!")
                elif guess < result:
                    print("Too small!")
                else:
                    print("Just right!")
                    break


main()
