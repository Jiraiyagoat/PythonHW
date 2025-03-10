word = input("Enter a string: ")
new_word = ""
length = len(word)
while(length != 0):
    new_word += word[length-1]
    length -= 1
if new_word == word:
    print("String is palindrome")
else:
    print("Strign is not palindrome")