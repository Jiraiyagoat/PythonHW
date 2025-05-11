tuple1 = tuple(input("Enter your list: ").split())
list1 = list(tuple1)
largest = list1[0]
for x in list1:
    if x > largest:
        largest = x
print(largest)