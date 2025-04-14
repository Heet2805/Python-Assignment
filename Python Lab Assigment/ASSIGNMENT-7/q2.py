import random
random_numbers = set()
while len(random_numbers) < 10:
    random_numbers.add(random.randint(15, 45))
    print("Original Set:", random_numbers)
count_less_than_30 = sum(1 for num in random_numbers if num < 30)
print("Count of numbers less than 30:", count_less_than_30)
numbers_to_remove = {num for num in random_numbers if num > 35}
random_numbers -= numbers_to_remove