set1 = set(input("Enter your set1: ").split())
set2 = set(input("Enter your set2: ").split())
if set2.issubset(set1):
    print("Exists")
else:
    print("Not exists")