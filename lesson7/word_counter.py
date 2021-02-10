# split by default separates both by space and line feed,
# just to enter the line feed command you need from sys import stdin
text = input('Input text please: ')
text = text.split()
new_text = []
for word in text:
    flag = False
    for char in word:
        if char.isalpha():
            flag = True
    if flag:
        new_text.append(word)
print(f'{len(new_text)} words is in your text')
