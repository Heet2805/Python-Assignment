import random
this_list = [random.randint(-30, 30) for _ in range(50)]
print(f"Generated list:{this_list}")
positive_list = [num for num in this_list if num>0]
print(positive_list)
negative_list = [num for num in this_list if num<0]
print(negative_list)
