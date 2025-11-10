# CSV to Database Importer

#### Video Demo: https://youtu.be/kx8B2doGnFQ

## Description

The CSV to Database Importer is a Python project that helps take information from a CSV file and put it into a SQLite database. I made this project as my final project for the CS50 Python course. The goal of the project is to show that I can read files, clean and check data, and store it in a database in an organized way.

In real life, data often comes in CSV files that might have mistakes or weird formatting. This project makes sure the data is cleaned and standardized before it goes into the database. For example, names are capitalized correctly, emails are all lowercase, postal codes are fixed, and dates are checked to make sure they are valid. If a date is wrong, it is replaced with an empty value so it doesn’t break the program.

The program is written in a file called `project.py`. The main function, `main()`, does everything: it connects to the database, creates tables if they don’t exist, reads the CSV file, cleans the data row by row, and inserts it into the database tables.

## Database Design Rationale

I decided to split the CSV data into **three different tables** in the database because it makes it easier to manage user information:

1. **Users table**: stores the main information like first name, last name, date of birth, and email. This keeps all the basic info in one place.
2. **Contacts table**: stores phone numbers. I put this in a separate table because a user can have more than one phone number. If I kept phone numbers in the first table, there would be empty cells for users who only have one or no phone number.
3. **Address table**: stores the user’s addresses (street, city, state, postal code, and country). I put this in its own table so a user can have multiple addresses without making the users table messy.

## Helper Functions

The program has three main helper functions:

- `read_csv(file)`: reads the CSV file and returns the data as a list of dictionaries.
- `clean_row(row)`: cleans and validates each row of data.
- `insert_row(conn, row)`: inserts the cleaned row into the correct tables in the database.

## Testing

The project also has automated tests using `pytest` in a file called `test_project.py`. The tests check that CSV reading, data cleaning, and database insertion all work correctly. It even uses a temporary in-memory database so tests don’t affect the real database.

## Learning Outcomes

This project taught me a lot about Python programming, like handling files, working with strings, managing errors, creating databases, and writing tests. It also shows why organizing data in separate tables can be helpful, especially when users can have multiple phone numbers or addresses.

## Conclusion

The CSV to Database Importer is a practical tool for cleaning and storing data. I strived to follow good programming practices and write a project can be used for real-world data management tasks.
