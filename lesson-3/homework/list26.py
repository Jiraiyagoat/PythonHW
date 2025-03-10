lists = input("Enter your list: ").split()
if len(lists) % 2 != 0:
    print("Middle element: ", lists[len(lists)//2])
else:
    print("Middle elements: ", lists[len(lists) // 2 - 1], lists[len(lists) // 2])