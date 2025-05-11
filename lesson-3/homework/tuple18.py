tuple1 = tuple(input("Enter: ").split())
start_in = int(input("Start index: "))
end_in = int(input("End index: "))
subtuple = tuple1[start_in:end_in+1]
min_el = min(subtuple)
print(min_el)