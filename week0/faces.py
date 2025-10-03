def main():
    user_input = input()
    faces = convert(user_input)
    print(faces)

def convert(text):
    emoji = text.replace(":)", "🙂").replace(":(", "🙁")
    return emoji

main()
