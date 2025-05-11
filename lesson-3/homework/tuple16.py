tuple1 = tuple(input("Enter your list: ").split())
list1 = list(tuple1)
list2 = list(tuple1)
list2.sort()
if list1 == list2:
    print("Sorted")
else:
    print("Not sorted")