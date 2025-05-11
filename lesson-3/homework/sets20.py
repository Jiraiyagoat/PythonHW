set1 = set(input("Enter your set1: ").split())
set2 = set(input("Enter your set2: ").split())
if set1.isdisjoint(set2):
    print("Yes disjoint")
else:
    print("Not disjoint")