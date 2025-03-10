lists = input("Enter your list: ").split()
un_list = []
for x in lists:
    if x not in un_list:
        un_list.append(x)
print(un_list)