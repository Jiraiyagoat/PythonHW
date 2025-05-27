dictionary = {
    'name': 'Xojiakbar', 
    'age': 18,
    'city': 'Tashkent', 
    'job': 'SAT Tutor',
    'hobby' : 'Video Games'
}
key = input("Enter the key you want to remove: ")
if key in dictionary:
    dictionary.pop(key)
    print(dictionary)
else:
    print("The key does not exist in the dictionary")