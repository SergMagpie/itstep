text = 'lorem ipsum dolor sit amet amet amet'
words = text.split()
longest_word=words[0]
often_word=words[0]
for word in words:
    if len(longest_word) < len(word):
        longest_word = word
    if words.count(often_word) < words.count(word):
        often_word = word
print('Чаще ',often_word,'Длиннее ',longest_word)
    
