tuple1 = tuple(input("Enter your list: ").split())
element = input("Enter element: ")
indices = [index for index, x in enumerate(tuple1) if x == element]
print(f"The element '{element}' appears at indices: {indices}")
