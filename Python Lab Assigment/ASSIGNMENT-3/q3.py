str = "Hello123"
alphabets = 0
digits = 0
for char in str:
    if char.isalpha():
        alphabets+=1
    elif char.isdigit():
        digits+=1

print("the number of alphabets are :" , alphabets)
print("the number of digits are :" , digits)





        