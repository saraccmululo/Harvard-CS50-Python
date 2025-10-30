months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
month_names = {}
# Assign each month a number manually
for i in range(len(months)):
    month_names[months[i]] = i + 1

def main():
    n = convert_date("Date: ")
    print(n)


def convert_date(prompt):
    while True:
        user_input = input(prompt).strip()
        if "/" in user_input:
            version1_input = user_input.split("/")
            if len(version1_input) !=3:
                continue
            month, day, year = version1_input[0], version1_input[1], version1_input[2]
            if not (month.isdigit() and day.isdigit() and year.isdigit()):
                continue
            if 0 < int(day) <= 31 and 0 < int(month) <= 12 and int(year) >= 1300:
                formatted_date = format_date(int(year), int(month), int(day))
                return formatted_date

        else:
            version2_input = user_input.split(" ")
            if len(version2_input) != 3:
                continue
            month, day, year = version2_input[0], version2_input[1], version2_input[2]
            if month not in month_names:
                continue
            if not day.endswith(","):
                continue
            new_day = day[:-1]
            day = new_day
            if not (day.isdigit() and year.isdigit()):
                continue
            month_number = month_names[month]
            day = int(day)
            year = int(year)
            if 1 <= day <= 31 and year >= 1300:
                return format_date(year, month_number, day)


def format_date(y, m, d):
    return f"{y}-{m:02}-{d:02}"


main()
