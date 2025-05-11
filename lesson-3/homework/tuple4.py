tuple1 = tuple(input("Enter your list: ").split())
element = input("Enter your element: ")
list1 = list(tuple1)
if element in list1:
    print("Present")
else:
    print("Not present")