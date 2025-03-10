lists = input("Enter your list: ").split()
num = int(input("Enter your number: "))
rep_list = []
for x in lists:
    for i in range(num):
        rep_list.append(x)
print(rep_list)