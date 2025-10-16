user_input = input("Greeting: ")
greeting = user_input.strip().lower()
if greeting.startswith("hello"):
    print("$0")
elif greeting[0] == "h":
    print("$20")
else:
    print("$100")
