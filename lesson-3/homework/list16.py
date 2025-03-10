lists = input("Enter list of numbers: ").split()
count = 0
for num in lists:
    if int(num) % 2 != 0:
        count += 1
print("There are", count, "odd numbers in list")