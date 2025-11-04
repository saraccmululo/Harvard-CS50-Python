mport re


def main():
    print(count(input("Text: ")))


def count(s):
    pattern=r"\bum\b"

    matches=re.findall(pattern,s, re.IGNORECASE)#returns an array of strings found

    return len(matches)


if __name__ == "__main__":
    main()
