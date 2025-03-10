lists = input("Enter your list: ").split()
element = input("Enter element to find: ")
indices = []
for i in range(len(lists)):
    if lists[i] == element:
        indices.append(i)
print(indices)
