dictionary1 = {
    'name': 'Xojiakbar', 
    'age': 18,
    'city': 'Tashkent', 
    'job': 'SAT Tutor',
    'hobby' : 'Video Games'
}

dictionary2 = {
    'name': 'D', 
    'age': 15,
    'home': 'London', 
    'work': 'Student'
}
set1 = set()
set2 = set()
for key in dictionary1.keys():
    set1.add(key)
for key in dictionary2.keys():
    set2.add(key)
set3 = set1.intersection(set2)
print(set3)