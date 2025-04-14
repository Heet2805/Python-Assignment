students = [(101 , "abc , 18") , (102,"def" , 19) , (103 , "ghi" , 19)]

roll_nos = []
ages = []
names  = []

for student in students:
    roll_no , age , name = student
    roll_nos.append(roll_no)
    names.append(name)
    ages.append(age)
    
    print("Roll no:" , roll_nos)
    print("Age:" , ages)
    print("names:" , names)