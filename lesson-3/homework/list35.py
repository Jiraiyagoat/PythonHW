start = int(input("Enter start of the range: "))
end = int(input("Enter end of the range: "))
lists = []
while start <= end:
    lists.append(start)
    start += 1
print(lists)