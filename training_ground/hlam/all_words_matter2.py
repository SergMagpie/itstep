text = '''Torches are made to light, jewels to wear,
Dainties to taste, fresh beauty for the use,
Herbs for their smell, and sappy plants to bear;
Things growing to themselves are growth’s abuse,
Seeds spring from seeds, and beauty breedeth beauty;
Thou wast begot; to get it is thy duty.'''

text_split = text.split()
upper_text = []
for word in text_split:
    if word[0].isalpha():
        word = word[:1].upper()+word[1:]
    upper_text.append(word)
print(*upper_text)