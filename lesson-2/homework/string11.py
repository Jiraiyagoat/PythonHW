word = input("Enter your string: ")
digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] 
digit = False
for char in word:
    if char in digits:
        digit = True
        break
    else:
        digit = False
if digit:
    print("There is digit")
else:
    print("There is no digit")