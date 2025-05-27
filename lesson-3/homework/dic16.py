dictionary = {
    'name': 'Xojiakbar', 
    'age': 18,
    'city': 'Tashkent', 
    'job': 'SAT Tutor',
    'hobby' : 'Video Games'
}
isNested = False
for value in dictionary.values():
    if type(value) == dict:
        isNested = True
if isNested:
    print("The dictionary is nested dictionary")
else:
    print("The dictionary is not nested")