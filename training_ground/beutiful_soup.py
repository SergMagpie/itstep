from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

# скачиваем файл
resp = urlopen('https://stepik.org/media/attachments/lesson/209723/4.html')
html = resp.read().decode('utf8')  # считываем содержимое
soup = BeautifulSoup(html, 'html.parser')  # делаем суп
s = soup.find_all('td')
print(s)
# print(sum(list(int(i.renderContents()) for i in s)))


# table = soup.find('table', attrs = {'class' : 'wikitable sortable'})
# cnt = 0
# for tr in soup.find_all('tr'):
#     cnt += 1
#     for td in tr.find_all(['td', 'th']):
#         cnt *= 2
# print(cnt)
