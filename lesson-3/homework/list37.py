lists = input("Enter your list: ").split()
total = 0
for x in lists:
    if int(x) < 0:
        total += int(x)
print(total)