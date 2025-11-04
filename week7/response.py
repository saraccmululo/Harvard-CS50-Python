from validator_collection import checkers

def main():
    email=input("What's your email address? ")
    is_email_address = checkers.is_email(email)
    response= "Valid" if is_email_address else "Invalid"
    print(response)


if __name__ == "__main__":
    main()
