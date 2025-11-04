import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    pattern=r"^(0?[1-9]|1[0-2]):?([0-5][0-9])?\s+(AM|PM)\s+to\s+(0?[1-9]|1[0-2]):?([0-5][0-9])?\s+(AM|PM)$"

    match=re.search(pattern, s)
    if match:
        hour1, min1, period1, hour2, min2, period2 = match.groups()
        # if minutes are missing, make it "00"
        min1 = min1 or "00"
        min2 = min2 or "00"

        work_from=format_hour(hour1, min1, period1)
        work_to=format_hour(hour2, min2, period2)

        return f"{work_from} to {work_to}"
    else:
        raise ValueError("Invalid time format")

def format_hour(hour, min, period):
    hour = int(hour)
    min =int(min)
    if period=="AM":
        if hour == 12:
            hour=0
    elif period=="PM":
        if hour !=12:
            hour=hour+12

    #adding leading zeroes{n:02}:if n is a single digit, it'll be prefixed with one 0
    return f"{hour:02}:{min:02}"

if __name__ == "__main__":
    main()