import sqlite3
import sys
from datetime import datetime
import csv
import string


def main():
    #connects with sqlite3
    conn = sqlite3.connect("user_data.db")

    # create table if not exists
    conn.execute("""
                CREATE TABLE IF NOT EXISTS users (
                 user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                 first_name VARCHAR(100),
                 last_name VARCHAR(100),
                 date_of_birth DATE,
                 email VARCHAR(100)
                 )
                 """)
    conn.execute("""
                CREATE TABLE IF NOT EXISTS contacts (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 user_id INTEGER,
                 phone VARCHAR(20)
                 )
                """)
    conn.execute("""
                CREATE TABLE IF NOT EXISTS address (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 user_id INTEGER,
                 address VARCHAR(100),
                 city VARCHAR(50),
                 state VARCHAR(20),
                 postal_code VARCHAR(10),
                 country VARCHAR(15)
                 )
                """)


    # Validate command-line
    if len(sys.argv) < 2:
        sys.exit("Too few arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many arguments")
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a .csv file")

    # Read and process CSV
    file = sys.argv[1]
    rows = read_csv(file)

    with conn:
        for row in rows:
            try:
                cleaned_row=clean_row(row)
                insert_row(conn, cleaned_row)
                print("Data inserted successfully!")
            except ValueError as e:
                print(f"Data cleaning failed: {e}")
            except sqlite3.IntegrityError as e:
                print(f"Database constraint error: {e}")
            except sqlite3.OperationalError as e:
                print(f"Database operational error: {e}")


def read_csv(file):
    """Read CSV file and return list of rows (as dicts)."""
    try:
        data_list = []
        with open(file, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data_list.append(row)
            return data_list

    except FileNotFoundError:
        sys.exit("CSV file not found")


def clean_row(row):
    """Clean the data row before inserting to db."""
    # Names
    row['user_id'] = row['user_id'].strip()
    row['first_name'] = string.capwords(row['first_name'].strip())
    row['last_name'] = string.capwords(row['last_name'].strip())
    # Date of birth
    row['date_of_birth'] = row['date_of_birth'].strip()
    try:
        datetime.strptime(row['date_of_birth'], "%Y-%m-%d")
    except ValueError:
        row['date_of_birth'] = ""

    # Email
    row['email'] = row['email'].lower()
    # Phone
    row['phone'] = row['phone'].strip()

    # Address
    row['address'] = string.capwords(row['address'].strip())
    row['city'] = string.capwords(row['city'].strip())
    row['state'] = string.capwords(row['state'].strip())
    row['country'] = string.capwords(row['country'].strip())

    # Postal Code
    row['postal_code'] = row['postal_code'].strip().replace(" ", "").upper()

    return row

def insert_row(conn, row):
    """Insert one data row into the database."""
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (user_id, first_name, last_name, date_of_birth, email) VALUES (?, ?, ?, ?, ?)",
        (row['user_id'], row['first_name'], row['last_name'], row['date_of_birth'], row['email'])
    )
    cursor.execute(
        "INSERT INTO contacts (user_id, phone) VALUES (?, ?)",
        (row['user_id'], row['phone'])
    )
    cursor.execute(
        "INSERT INTO address (user_id, address, city, state, postal_code, country) VALUES (?, ?, ?, ?, ?, ?)",
        (row['user_id'], row['address'], row['city'],row['state'], row['postal_code'], row['country'])
    )
    conn.commit()


if __name__ == "__main__":
    main()
