alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
rot_alphabet = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
text = input('Input text, please: ')
new_text = ''
for char in text:
    if char in alphabet:
        char = rot_alphabet[alphabet.find(char)]
    new_text += char
print('Encrypted message:', new_text)
