# Create two dictionaries – one containing grocery items and their prices and another containing grocery items and quantity purchased. By using the values from these two dictionaries compute the total bill.

grocery_prices = {
    'apple': 2.5,
    'banana': 1.0,
    'orange': 1.5,
    'milk': 3.0,
    'bread': 2.0
}
grocery_quantities = {
    'apple': 3,
    'banana': 5,
    'orange': 2,
    'milk': 1,
    'bread': 4
}


def calculate_total_bill(prices, quantities):
    total_bill = 0
    for item, price in prices.items():
        if item in quantities:
            total_bill += price * quantities[item]
    return total_bill


total_bill = calculate_total_bill(grocery_prices, grocery_quantities)
print(f"Total bill: ${total_bill:.2f}")  # Output: Total bill: $22.50
