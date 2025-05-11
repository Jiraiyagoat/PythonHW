import random
size = int(input("Enter the number of random elements: "))
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

if size > (end - start + 1):
    print("Size cannot be larger than the range of numbers!")
else:
    random_set = set(random.sample(range(start, end + 1), size))
    print(random_set)
