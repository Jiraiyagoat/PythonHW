tuple1 = tuple(input("Enter your list: ").split())
number = int(input("Enter number: "))
tuple2 = tuple(element for element in tuple1 for _ in range(number))
print(tuple2)
