a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a==b or b==c or c==a:
    print("Numbers are equal")
elif (a>b) and (a>c):
    print(f"{a} is largest")
elif (b>a) and (b>c):
    print(f"{b} is largest")
else:
    print(f"{c} is largest")
