import random
this_list = [random.randint(1,100) , range(20)]
print(this_list)
input_no = int(input("Enter the number:"))
print(input_no)
position = [index for index, value in enumerate(this_list) if value == input_no]
if position:
    print(position)
else:
    print("not found")
