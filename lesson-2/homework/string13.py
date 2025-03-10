words = input("Enter your string: ").split(" ")
merged_w = ""
for x in range(len(words)):
    merged_w += words[x]
print(merged_w)