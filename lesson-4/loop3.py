text = input("Enter a string: ")
vowels = {'a', 'e', 'i', 'o', 'u'}
result = []
i = 0
count = 0
while i < len(text):
    result.append(text[i])
    count += 1
    if count % 3 == 0 and i < len(text) - 1:
        if text[i] in vowels:
            i += 1
            if i < len(text):
                result.append(text[i])
                result.append('_')
        else:
            result.append('_')
    i += 1
if result and result[-1] == '_':
    result.pop()
print(''.join(result))
