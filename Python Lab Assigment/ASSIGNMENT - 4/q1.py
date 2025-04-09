this_list1 = [1,3,5,7,9]
this_list2 = [2,4,6,8]
this_list1[2] = this_list2
print(this_list1)
flattened_list = []
for item in this_list1:
    if isinstance(item, list):  # Flatten nested lists
        flattened_list.extend(item)
    else:
        flattened_list.append(item)

print(f"Flattened list: {flattened_list}")

# Step 5: Sort the flattened list
sorted_list = sorted(flattened_list)
print(f"Sorted list: {sorted_list}")
