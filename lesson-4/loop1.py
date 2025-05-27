list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]
uncommon = []
list2_copy = list2.copy()
for item in list1:
    if item in list2_copy:
        list2_copy.remove(item)
    else:
        uncommon.append(item)
uncommon += list2_copy
print(uncommon)
