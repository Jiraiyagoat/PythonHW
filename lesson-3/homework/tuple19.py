tuple1 = tuple(input("Enter your list: ").split())
element = input("Enter element: ")
if element in tuple1:
    index = tuple1.index(element)
    new_tuple = tuple1[:index] + tuple1[index+1:]
    print(new_tuple)
else:
    print("Element not found in the tuple.")
