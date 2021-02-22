from urllib import urlopen
html = urlopen("https://stepik.org/media/attachments/lesson/209717/1.html").read()
s = str(html)
print(s.count("..."))