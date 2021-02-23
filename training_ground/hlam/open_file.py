s = open('text.txt', 'r', encoding='utf8').read()
print(s[s.find('<code>'):s.find('<code>') + 6])
print(s.find('<code>'))
print(s.find('</code>'))
print(s[5:].find('<code>'))
text = s
n = 0
entry = text[text[n:].find('<code>') + 6:text[n:].find('</code>')]
print(entry)
print(n)
