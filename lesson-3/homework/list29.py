lists = input("Enter your list: ").split()
index = int(input("Enter your index: "))
if index < 0 or index > len(lists):
    print("Invalid index")
else:
    lists.pop(index)
    print(lists)