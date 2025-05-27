dictionary = {
    'name': 'Xojiakbar', 
    'age': 18,
    'city': 'Tashkent', 
    'job': 'SAT Tutor',
    'hobby' : 'Video Games'
}
key = input("What are you looking for? ")
if key in dictionary:
    print("The key is present in the dictionary.")
else:
    print("The key is not present in the dictionary.")