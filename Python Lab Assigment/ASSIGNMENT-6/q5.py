prices = {
    "apple" : 40,
    "banana":50,
    "cherry": 60
}

quantity = {
    "apple": 3,
    "banana":5,
    "cherry":6
}

total_bill = 0
for item in prices:
    if item in quantity:
        item_total = prices[item] * quantity[item]
        total_bill += item_total

        print(total_bill)
