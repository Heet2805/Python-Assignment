length = int(input("Enter length"))
width = int(input("Enter width"))

ar = length * width
peri = (len+width) * 2

if ar > peri:
    print("Area is greater than peri")
elif ar == peri:
    print("Area is equal to peri")
else:
    print("Area is less than peri")