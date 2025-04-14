names = ["alice" , ("nosidn",) , "oienoc" , ("oiwen",) , "oien"]

boys  = 0
girls = 0
for name in names:
    if isinstance(name,tuple):
        boys =+ 1
    
else:
    girls =+1

    print("number of the boys:",boys)
    print("the number of girls:",girls)