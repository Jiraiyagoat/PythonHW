set1 = set(input("Enter your set1: ").split())
element = input("Enter your element: ")
if element not in set1:
    set1.add(element)
    print(set1)
else:
    print("Already in set")