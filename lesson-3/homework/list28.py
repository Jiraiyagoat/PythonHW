lists = input("Enter your list: ").split()
start = int(input("Enter start index: "))
end = int(input("Enter end index: "))
if start > end or start < 0 and end >= len(lists):
    print("Invalid start and end")
else:
    sublist = lists[start:end+1]
    min_el = sublist[0]
    for x in sublist:
        if x <= min_el:
            min_el = x
    print("Min of sublist is", min_el)
