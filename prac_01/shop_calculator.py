def calculate_total_price():
    total_price = 0.0

    while True:
        try:
            num_items = int(input("Number of items: "))
            if num_items >= 0:
                break
            else:
                print("Invalid number of items! Please enter a non-negative value.")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

    for item_number in range(1, num_items + 1):
        try:
            item_price = float(input(f"Price of item {item_number}: "))
            total_price += item_price
        except ValueError:
            print("Invalid input! Please enter a valid floating-point number.")

    if total_price > 100:
        total_price *= 0.9

    print(f"Total price for {num_items} items is ${total_price:.2f}")


if __name__ == "__main__":
    calculate_total_price()
