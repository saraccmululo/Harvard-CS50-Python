def main():
    time = input("What time is it? ")
    result=convert(time)

    if 7.0<=result<=8.0:
        print("breakfast time")
    if 12.0<=result<=13.0:
        print("lunch time")
    if 18.0<=result<=19.0:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    h=float(hours)
    m=float(minutes)/60
    return h+m


if __name__ == "__main__":
    main()
