yr = int(input("Enter a year: "))

if yr %4 ==0 and yr%100 == 0 and yr%400 == 0:
    print(f"{yr} is a leap year.")