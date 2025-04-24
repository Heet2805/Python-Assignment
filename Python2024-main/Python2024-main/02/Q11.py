def check_collinear(p1,p2,p3):
    area = p1[0]*(p2[1]-p3[1]) - p2[0]*(p1[1]-p3[1]) + p3[0]*(p1[1] - p2[1])
    if area == 0:
        print("Points lie on a straight line")
    else:
        print("Points do not lie on a straight line")
    
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))
x3 = int(input("Enter x3: "))
y3 = int(input("Enter y3: "))

check_collinear((x1,y1),(x2,y2),(x3,y3))