this_list = [("apple" , 10) , ("banana" , 12) , ("chips" , 100)]

this_list.sort(key=lambda item: item[1] , reverse=True)
for food , price in this_list:
    print(f"{food}:${price:.2f}")
    
          