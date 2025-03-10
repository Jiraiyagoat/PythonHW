lists = input("Enter your list: ").split()
list_odd = []
for x in lists:
    if int(x) % 2 != 0:
        list_odd.append(int(x))
print(list_odd)