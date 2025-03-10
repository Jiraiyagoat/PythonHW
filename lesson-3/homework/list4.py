numbers = input("Enter your numbers: ").split()
smallest = int(numbers[0])
for num in numbers:
    if int(num) < smallest:
        smallest = int(num)
print("The smallest number is:", smallest)