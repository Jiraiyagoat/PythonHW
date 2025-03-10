numbers = input("Enter 3 numbers (with space between them): ").split()
num1 = int(numbers[0])
num2 = int(numbers[1])
num3 = int(numbers[2])
if num1 == num2 == num3:
    print("They are not different")
else:
    print("They are different")
