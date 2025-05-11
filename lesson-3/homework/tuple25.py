tuple1 = tuple(input("Enter your list: ").split())
unique_elements = []
for element in tuple1:
    if element not in unique_elements:
        unique_elements.append(element)
unique_tuple = tuple(unique_elements)
print("Tuple with unique elements in original order:", unique_tuple)
