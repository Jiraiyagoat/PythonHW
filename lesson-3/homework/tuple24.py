tuple1 = tuple(input("Enter your list: ").split())
if tuple1 == tuple1[::-1]:
    print("yes")
else:
    print("no")