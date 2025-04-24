a = 10
b = 20
# 1 Add two numbers
print("Add = ", a+b)
# 2 Subtract two numbers
print("Sub = ", b-a)
# 3 Multiply two numbers
print("Mul = ", a*b)
# 4 Divide two numbers
print("Div = ", a/b)
# 5
print("Add = ", a+b)
print("Sub = ", b-a)
print("Mul = ", a*b)
print("Div = ", a/b)
# 6 Convert hours into minutes
hr = int(input("Enter hr = "))
print(hr,"hr =", 60*hr, "mins")
# 7 Convert minutes into hours
min = int(input("Enter mins = "))
print(min,"mins = ", min/60, "hrs")
# 8 Convert rs into dollars
rs = int(input("Enter rs = "))
print(rs, "rs = ", rs/48,"Dollars")
# 9 Convert dollars into rs
dl = int(input("Enter dollar = "))
print(dl,"dollars = ", dl*48, "rs")
# 10 Convert dollars into pound
dl = int(input("Enter dollar = "))
print(dl,"dollars = ", dl*48/70, "pound")
# 11 Convert grams into kgs
gm = int(input("Enter grams = "))
print(gm,"grams = ", gm/1000, "kg")
# 12 Convert kgs into grams
kg = int(input("Enter kgs ="))
print(kg,"kg = ", kg*1000, "gms")
# 13 Convert bytes into Kb, Mb, Gb
byt = int(input("Enter bytes = ")) 
print(f"{byt}bytes = {byt/1000}Kb, {byt/1000000}Mb, {byt/(1000*1000*1000)}Gb")
# 14 Convert celcius into fahrenheit
cel =int(input("Enter celcius = "))
print(f"{cel}celcius = {((9/5)* cel)+32}fahrenheit")
# 15 Convert fahrenheit int celcius
f =int(input("Enter fahrenheit = "))
print(f"{f}fahrenheit = {(5/9)*(f -32)}celcius")
# 16 Calculate interest
p = int(input("Enter p ="))
r = int(input("Enter r ="))
n = int(input("Enter n ="))
print(f"Interest = {(p*r*n)/100}")
# 17 Calculate area & perimeter of a square
s = int(input("Enter side len = "))
print(f"Enter area = {s*s}, perimeter = {4*s}")
# 18 Calculate area & perimeter of a rectangle
s1 = int(input("Enter side len = "))
s2 = int(input("Enter side len = "))
print(f"Enter area = {s1*s2}, perimeter = {(2*s1 )+ (2*s2)}")
# 19 Calculate area of a circle
r = int(input("Enter radius = "))
print(f"Area = {3.14 * r*r}")
# 20 Calculate area of a triangle
h =int(input("Enter h = "))
l =int(input("Enter l = "))
print("Area = ", (h*l)/2)
# 21 Calculate net salary (net salary = gross salary + allowance - deduction)
gs = int(input("Enter Gross Salary = "))
al = gs *0.1
de = gs * 0.03
print("Net salary = ", gs + al - de)
# 22 Calculate net sales where net sales = gross sales - 10% discount
gs = int(input("Enter Gross Salary = "))
print("Enter net sales = ", gs - (0.1*gs))
# 23 Calculateaverage of three subjects along with their total 
sb1 = int(input("Subject 1 = "))
sb2 = int(input("Subject 2 = "))
sb3 = int(input("Subject 3 = "))
print("Total = ", sb1+sb2+sb3)
print("Avg = ", (sb1+sb2+sb3)/ 3)
# 24 Swap two values
a = 10
b = 22
print("a =", a, "b =", b)
a,b=b,a
print("a =", a, "b =", b)
