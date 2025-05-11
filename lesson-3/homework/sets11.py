set1 = set(input("Enter your set1: ").split())
set2 = set(input("Enter your set2: ").split())
set3 = set1.symmetric_difference(set2)
print(set3)