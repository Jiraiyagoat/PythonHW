words = input("Enter your words: ").split(" ")
merged_w = ""
for x in range(len(words)):
    merged_w += words[x]
    if x != len(words) - 1:
        merged_w += ","
    else:
        break
print(merged_w)