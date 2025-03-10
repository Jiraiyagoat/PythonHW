word1 = input("Enter main string: ").lower()
word2 = input("Enter checking string: ").lower()
if word2 in word1:
    print("Exists")
else:
    print("Does not exist")