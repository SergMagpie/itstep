from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

# скачиваем файл
resp = urlopen('https://stepik.org/media/attachments/lesson/209723/5.html')
html = resp.read().decode('utf8')  # считываем содержимое
soup = BeautifulSoup(html, 'html.parser')  # делаем суп
s = soup.find_all(text=True)
print(sum([int(i.strip()) for i in s if i.strip().isdigit()]))
