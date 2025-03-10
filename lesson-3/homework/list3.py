numbers = input("Enter your numbers: ").split()
largest = int(numbers[0])
for num in numbers:
    if int(num) > largest:
        largest = int(num)
print("The largest number is:", largest)