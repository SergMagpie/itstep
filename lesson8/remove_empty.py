list_with_strings = ['gdsfdss', ' ', 'dscsd',
                     '.', 6, '\n', ['fcv'], {3: '33'}, '']
list_without_strings = []
for item in list_with_strings:
    if str(item).isspace() or not item:
        continue
    else:
        list_without_strings.append(item)
print(list_without_strings)
