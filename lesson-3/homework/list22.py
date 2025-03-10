lists = input("Enter your list: ").split()
list_even = []
for x in lists:
    if int(x) % 2 == 0:
        list_even.append(int(x))
print(list_even)