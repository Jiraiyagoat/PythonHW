lists = input("Enter your list: ").split()
element = input("Enter your element: ")
replace = input("Enter your replacement: ")
for x in lists:
    if x == element:
        lists[lists.index(x)] = replace
print(lists)