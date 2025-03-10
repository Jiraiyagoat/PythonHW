word = input("Enter your string: ")
vowels = ["a", "o", "i", "u", "e"]
new_word = ""
for char in word:
    if char.lower() in vowels:
        new_word += "*"
    else:
        new_word += char
print(new_word)