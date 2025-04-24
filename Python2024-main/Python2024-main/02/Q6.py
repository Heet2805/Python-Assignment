def digits(n, len):
    n= n//10
    len += 1
    if n > 0:
        return digits(n,len)
    else:
        print(f"Given number contains {len} digits")

num = int(input("Enter a number: "))
digits(num, 0)