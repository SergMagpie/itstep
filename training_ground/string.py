text = '''Torches are made to light, jewels to wear,
Dainties to taste, fresh beauty for the use,
Herbs for their smell, and sappy plants to bear;
Things growing to themselves are growth’s abuse,
Seeds spring from seeds, and beauty breedeth beauty;
Thou wast begot; to get it is thy duty.'''
cont_sentence = 0
cont_punkt = 0
for i in text:
    if i in '.,;:?':
        cont_punkt += 1
    if i == '.':
        cont_sentence += 1
print('cont sentence: {}'.format(cont_sentence))
print('cont punkt: {}'.format(cont_punkt))
