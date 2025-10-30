def main():
    x = calculate_price("Item: ")
    print(f"${x:.2f}\n")


items = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

lower_items = {}
for item in items:
    lower_item = item.lower()
    lower_items[lower_item] = items[item]

def calculate_price(prompt):
    total_price = 0
    while True:
        try:
            user_input = input(prompt)
            lower_input = user_input.lower()

            if lower_input in lower_items:
                price = lower_items[lower_input]
                total_price += price
                print(f"${total_price:.2f}")
            else:
                pass
        except KeyError:
            pass
        except EOFError:
            return total_price
main()
