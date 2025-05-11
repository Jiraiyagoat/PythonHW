tuple1 = tuple(input("Enter your list: ").split())
n = int(input("Enter the number of elements per subtuple: "))
nested_tuple = tuple(tuple1[i:i+n] for i in range(0, len(tuple1), n))
print("Nested tuple with subtuples:", nested_tuple)
