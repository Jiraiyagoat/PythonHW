list_m = input("Enter your main list: ").split()
list_s = input("Enter your sub list: ").split()
present = False
for i in range(len(list_m) - len(list_s) + 1):
    if list_m[i:i+len(list_s)] == list_s:
        present = True
        break
if present:
    print("Sub list exists")
else:
    print("Sub list doesn't exist")
