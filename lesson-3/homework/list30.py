lists = input("Enter your list: ").split()
lists_sor = lists.copy()
lists_sor.sort()
if lists == lists_sor:
    print(True)
else:
    print(False)