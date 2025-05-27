dictionary = {
    'name': 'Xojiakbar', 
    'age': 18,
    'city': 'Tashkent', 
    'job': 'SAT Tutor',
    'hobby' : 'Video Games'
}
list = []
for value in dictionary.values():
    if value not in list:
        list.append(value)
print("There are", len(list), "unique values in this dictionary")