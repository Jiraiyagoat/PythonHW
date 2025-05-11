set1 = set(input("Enter your set1: ").split())
element = input("Enter your element: ")
if element in set1:
    set1.remove(element)
    print(set1)
else:
    print("No such element in set")