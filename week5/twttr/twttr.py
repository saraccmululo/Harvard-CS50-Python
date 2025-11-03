def main():
    s = input("Input: ")
    print("Output:", shorten(s))

def shorten(word):
    twttr = ""
    for char in word:
        if char in "aeiou" or char in "AEIOU":
            continue
        else:
            twttr += char

    return twttr


if __name__ == "__main__":
    main()
