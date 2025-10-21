import sys
import csv

def main():

    if len(sys.argv)<3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv)>3:
        sys.exit("Too many command-line arguments")

    students=[]

    try:
        with open(sys.argv[1]) as file:
            reader=csv.DictReader(file)
            for row in reader:
                s=row["name"].split(",")
                first, last = s[1].strip(), s[0].strip()
                students.append({"first": first, "last": last, "house": row["house"]}) #output: {"name": "Bell, Katie", "house": "Gryffindor"}

        with open(sys.argv[2], "w") as file:
            writer=csv.DictWriter(file, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for student in students:
                writer.writerow(student)

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

if __name__=="__main__":
    main()
