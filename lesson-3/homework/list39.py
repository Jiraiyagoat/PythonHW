original_list = input("Enter the elements of the list separated by spaces: ").split()
sublist_size = int(input("Enter the size of each sublist: "))
nested_list = []
for i in range(0, len(original_list), sublist_size):
    nested_list.append(original_list[i:i + sublist_size])
print(nested_list)
