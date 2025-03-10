lists = input("Enter your list: ").split()
target = input("Enter the element to count: ")
count = 0
for item in lists:
    if item == target:
        count += 1
print(target, "appeared", count, " times")