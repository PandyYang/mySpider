import urllib.request
from bs4 import BeautifulSoup

url = "https://www.starbucks.com.cn/menu/"

response = urllib.request.urlopen(url)

content = response.read().decode('utf8')

soup = BeautifulSoup(content, 'lxml')

menu_list = soup.select('ul[class="grid padded-3 product"] strong')

with open('startbuck_menu.txt', 'w+', encoding='utf8') as fd:
    for name in menu_list:
        fd.write(name.get_text() + "\n")