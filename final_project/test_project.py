from project import read_csv, clean_row, insert_row
import sqlite3


def test_read_csv(tmp_path):
    # Create a temporary CSV file
    test_file = tmp_path/"test.csv"
    test_file.write_text("user_id,first_name,last_name,date_of_birth,email,phone,address,city,state,postal_code,country\n"
    "1, alice , smith ,1990-01-01,ALICE@EXAMPLE.COM,1234567890, 123 main st ,new york,ny,10001,usa\n")

    data=read_csv(str(test_file))
    assert len(data) == 1
    assert data[0]['first_name'].strip() =="alice"
    assert data[0]['last_name'].strip() == "smith"

def test_clean_row():
    row = {
        "user_id": "1",
        "first_name": " alice ",
        "last_name": "smith",
        "date_of_birth": "1990-01-01",
        "email": "ALICE@EXAMPLE.COM",
        "phone": " 1234567890 ",
        "address": " 123 main st ",
        "city": "new york",
        "state": "ny",
        "postal_code": "10001",
        "country": "usa"
    }

    cleaned=clean_row(row)
    assert cleaned['first_name'] == "Alice"
    assert cleaned['last_name'] == "Smith"
    assert cleaned['email'] == "alice@example.com"
    assert cleaned['address'] == "123 Main St"
    assert cleaned['city'] == "New York"
    assert cleaned['postal_code'] == "10001"


def test_insert_row():
    # Use in-memory SQLite database
    conn = sqlite3.connect(":memory:")

    # Create tables
    conn.execute("""
        CREATE TABLE users (
            user_id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            date_of_birth DATE,
            email TEXT
        )
    """)
    conn.execute("""
        CREATE TABLE contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            phone TEXT
        )
    """)
    conn.execute("""
        CREATE TABLE address (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            address TEXT,
            city TEXT,
            state TEXT,
            postal_code TEXT,
            country TEXT
        )
    """)

    row = {
        "user_id": "1",
        "first_name": "Alice",
        "last_name": "Smith",
        "date_of_birth": "1990-01-01",
        "email": "alice@example.com",
        "phone": "1234567890",
        "address": "123 Main St",
        "city": "New York",
        "state": "NY",
        "postal_code": "10001",
        "country": "USA"
    }

    insert_row(conn, row)

    # Check users table
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    assert len(users) == 1
    assert users[0][1] == "Alice"

    # Check contacts table
    cursor.execute("SELECT * FROM contacts")
    contacts = cursor.fetchall()
    assert len(contacts) == 1
    assert contacts[0][2] == "1234567890"

    # Check address table
    cursor.execute("SELECT * FROM address")
    addresses = cursor.fetchall()
    assert len(addresses) == 1
    assert addresses[0][2] == "123 Main St"

    conn.close()
