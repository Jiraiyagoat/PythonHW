dictionary = {
    'name': 'Xojiakbar', 
    'age': 18,
    'city': 'Tashkent', 
    'job': 'SAT Tutor',
    'hobby' : 'Video Games'
}
key = input("What are you looking for? ")
print(dictionary.get(key, "Not found"))