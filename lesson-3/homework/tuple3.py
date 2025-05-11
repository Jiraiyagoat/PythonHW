tuple1 = tuple(input("Enter your list: ").split())
list1 = list(tuple1)
min_el = list1[0]
for x in list1:
    if x < min_el:
        min_el = x
print(min_el)