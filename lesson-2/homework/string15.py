org_word = input("Enter your word: ").split(" ")
arc_w = ""
temp = ""
for x in range(len(org_word)):
    temp = org_word[x]
    arc_w += temp[0].upper()
print(arc_w)