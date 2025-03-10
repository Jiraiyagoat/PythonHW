vowels = ["a", "i", "o", "e", "u"]
consonants = ["q", "w", "r", "t", "y", "p",
              "s", "d", "f", "g", "h", "j",
              "k", "l", "z", "x", "c", "v",
              "b", "n", "m"]
vowels_num = 0
consonants_num = 0
word = input("Enter a string: ").lower()
for char in word:
    if char in vowels:
        vowels_num += 1
    elif char in consonants:
        consonants_num += 1
print("Number of vowels:", vowels_num)
print("Number of consonants:", consonants_num)
