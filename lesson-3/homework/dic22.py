ages = {
    'A': 27,
    'B': 21,
    'C': 10,
    'D': 39
}
copy = ages.copy()
for key, value in ages.items():
    if value < 18:
        copy.pop(key)
print(copy)