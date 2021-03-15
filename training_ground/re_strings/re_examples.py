import re

cach_str = "Cach CachCach"
digits_str = '123asdas d456'

pattern = re.compile(r'\s')

matches = pattern.finditer(digits_str)

for match in matches:
    print(match)

print(digits_str[10:11])