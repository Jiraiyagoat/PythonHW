word = input("Enter a string: ")
reversed_w = ""
for x in range(len(word)):
    reversed_w += word[len(word) - 1 -x]
print(reversed_w)
