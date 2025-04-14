dict_1 = { "a" : 1 , "b": 2 , "c":3 }
dict_2 = { "d" : 1 , "e": 2 , "f":3 }
dict_3 = { "g" : 1 , "h": 2 , "i":3 }
dict_4 = {**dict_1 , **dict_2 , **dict_3}
print(dict_4)