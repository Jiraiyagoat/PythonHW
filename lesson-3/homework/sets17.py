set1 = set(input("Enter your set1: ").split())
set2 = set()
for x in set1:
    if int(x) % 2 != 0:
        set2.add(int(x))
print(set2)