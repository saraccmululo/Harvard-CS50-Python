def main():
    user_input = input("Greeting: ")
    greeting = user_input.strip().lower()
    result=value(greeting)

    if result ==0:
        print("$0")
    elif result == 20:
        print("$20")
    else:
        print("$100")

def value(greeting):
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith == "h":
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()

