set1 = set(input("Enter your set1: ").split())
if set1:
    x = set1.pop()
    print("Popped: ",x)
    print(set1)
else:
    print("Set is empty")