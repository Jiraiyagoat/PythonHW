string = input("Enter a string: ")
char_rem = input("Enter a character to remove: ")
new_string = ""
for char in string:
    if char != char_rem:
        new_string += char
print("String after removal:", new_string)
