list1 = input("Enter your list: ").split()
list2 = []
for x in list1:
    if x not in list2:
        list2.append(x)
print(list2)