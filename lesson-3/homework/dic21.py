dictionary = {
    'name': 'Xojiakbar', 
    'city': 'Tashkent', 
    'job': 'SAT Tutor',
    'hobby' : 'Video Games'
}
sorted_dict = dict(sorted(dictionary.items(), key = lambda item: item[1]))
print(sorted_dict)