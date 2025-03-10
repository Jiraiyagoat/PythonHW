sentence = input("Enter your sentence: ")
word_rep = input("Enter a word to replace: ")
word_w = input("Enter a word to replcae with: ")
words = sentence.split()
for i in range(len(words)):
    if words[i] == word_rep:
        words[i] = word_w
        break
new_sentence = ""
for i in range(len(words)):
    new_sentence += words[i] + " "
print(new_sentence)