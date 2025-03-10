lists = input("Enter your list: ").split()
element = input("Enter element: ")
if element in lists:
    print(lists.index(element))
else:
    print("No such element in list")