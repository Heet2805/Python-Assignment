import math
n = int(input("Enter the values:"))
r = int(input("Enter the value:"))

nCr = math.comb(n,r)
nPr = math.perm(n,r)

print(nCr , nPr)
