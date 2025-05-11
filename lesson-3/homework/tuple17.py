tuple1 = tuple(input("Enter: ").split())
start_in = int(input("Start index: "))
end_in = int(input("End index: "))
subtuple = tuple1[start_in:end_in+1]
max_el = max(subtuple)
print(max_el)