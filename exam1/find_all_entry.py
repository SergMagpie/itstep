def find_all_entry(text, symbol):
    return [i for i, j in enumerate(text) if j == symbol]


text = "The core of extensible programming is defining functions."
print(find_all_entry(text, 'e'))
