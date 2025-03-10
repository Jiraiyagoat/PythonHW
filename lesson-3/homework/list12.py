lists = input("Enter your list: ").split()
element = input("Enter element to insert: ")
index = int(input("Enter the index: "))
if 0 <= index <= len(lists):
    lists.insert(index, element)
    print(lists)
else:
    print("Invalid index")