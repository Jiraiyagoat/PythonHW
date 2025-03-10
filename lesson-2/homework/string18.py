sentence = input("Enter your string: ").split()
first_w = input("First word: ")
last_w = input("Last word: ")
if sentence[0] == first_w and sentence[len(sentence) - 1] == last_w:
    print("Yes")
else:
    print("No")