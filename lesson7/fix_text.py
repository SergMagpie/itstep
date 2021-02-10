text = input('Input your text, please: ')
new_text = ''
flag = False
for char in text:
    if char == '.':
        flag = True
    if flag:
        if char.isalpha():
            char = char.upper()
            flag = False
    new_text += char
print('I edited your text:', new_text)
