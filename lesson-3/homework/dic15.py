keys = ['name', 'age', 'city', 'job']
values = ['Xojiakbar', 18, 'Tashkent', 'SAT Tutor']
dictionary = dict.fromkeys(keys, 'Unknown')
for i in range(len(dictionary)):
    dictionary[keys[i]] = values[i]
print(dictionary)