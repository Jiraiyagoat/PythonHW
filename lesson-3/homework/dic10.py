dictionary = {
    'name': 'Xojiakbar', 
    'age': 18,
    'city': 'Tashkent', 
    'job': 'SAT Tutor',
    'hobby' : 'Video Games'
}
key = input("Enter the key you are looking for: ")
if key in dictionary:
    print(key + ":", dictionary[key])
else:
    print("The key does not exist")