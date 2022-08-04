
from bs4 import BeautifulSoup

soup = BeautifulSoup(open('bs4_base.html', encoding='utf8'), 'lxml')

print(soup.a)