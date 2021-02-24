from typing import Counter
from urllib.request import urlopen
html = urlopen(
    "https://stepik.org/media/attachments/lesson/209719/2.html").read().decode('utf-8')
s = str(html)


def cut_tegs(s):
    flag = True
    s1 = []
    for i in s:
        if i == '<':
            flag = False
        if flag:
            s1.append(i)
        if i == '>':
            flag = True
    return ''.join(s1)


def get_code(text):

    s1 = []
    n = 0
    while '</code>' in text[n:]:
        entry = text[n + text[n:].find('<code>') +
                     6:n + text[n:].find('</code>')]
        k = text[n:].find('</code>')
        n += k + 7
        s1.append(entry)
    return s1


s3 = get_code(s)
s2 = Counter(s3)
print(*[i[0] for i in s2.most_common(3)])
