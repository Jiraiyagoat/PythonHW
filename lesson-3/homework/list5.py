lists = input("Enter your list: ").split()
target = input("Enter element to find: ")
present = False
for x in lists:
    if x == target:
        present = True
        break
if present:
    print(target, "is present in list")
else:
    print(target, "isn't in list")