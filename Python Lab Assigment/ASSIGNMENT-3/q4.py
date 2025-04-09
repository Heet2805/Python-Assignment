input_num = int(input('Enter the number:'))
#for prime
is_prime = True
if input_num < 2:
    is_prime = False

else:
    is_prime = True
    for i in range(2 , int(input_num/0.5)+1):
        if input_num%i == 0:
            is_prime = False
            break
if is_prime:
    print(f"{input_num} is a prime number")

else:
    print(f"{input_num} is not a prime number")


#for perfect
divisors_sum = 0 
for i in range(1,input_num):
    if input_num%i == 0:
        divisors_sum += i
if divisors_sum == input_num:
    print(f"{input_num} is a perfect number")
    
else:
    print(f"{input_num} is not a perfect number")

#Armstrong number
digits_sum = 0
temp_num = input_num
num_digits = len(str(input_num))
while temp_num > 0:
    digit = temp_num % 10
    digits_sum += digit ** num_digits
    temp_num //= 10

    if digits_sum == input_num:
        print(f"{input_num} is a armstrong number")

    else:
        print(f"{input_num} is not a armstrong number")

#for palindrome
temp_num = input_num
reversed_num = 0
while temp_num > 0:
    digit = temp_num & 10
    reversed_num = reversed_num * 10 + digit
    temp_num //= 10
if reversed_num == input_num:
    print(f"{input_num} is a palindrome.")
else:
    print(f"{input_num} is not a palindrome.")

#for automorphic number
last_digits = int(str(input_num ** 2)[-len(str(input_num)):])
if last_digits == input_num:
    print(f"{input_num} is an automorphic number.")
else:
    print(f"{input_num} is not an automorphic number.")


    



