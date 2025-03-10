lists = input("Enter your list: ").split()
if len(lists) < 2:
    print("Insufficient number of elements")
else:
    list2 = list(set(lists))
    list2.sort()
    print("Second smallest number: ", list2[1])
