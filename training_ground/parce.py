from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import re
req = Request('https://www.yakaboo.ua/search/?multi=0&cat=&q=python',
              headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read().decode('utf8')
soup = BeautifulSoup(webpage, 'html.parser')  # делаем суп
s = soup.find_all(attrs={'class': ['name', 'val']})
result = re.findall(r'title="(.+?)">', str(s))
result1 = re.findall(r'<span class="val">(\d{4})</span>', str(s))
print(*list(zip(result, result1)), sep=',\n')
