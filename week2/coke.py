print("Amount Due:50")
due = 50
payment = 0
change = None

while payment < 50:
    n = int(input("Insert Coin:"))
    if n == 25 or n == 10 or n == 5:
        payment = payment+n
        due = due - n
        if due <= 0:
            break
    print("Amount Due:", due)

if payment > 50:
    change = payment-50
if payment == 50:
    change = 0

print("Change Owed:", change)
