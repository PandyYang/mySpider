
import re
from bs4 import BeautifulSoup

soup = BeautifulSoup(open('bs4_base.html', encoding='utf8'), 'lxml')

print(soup.a)

name_pattern = re.compile(r'Summary</h2>(.*?)<', re.M)
with open('s001.html', 'r', encoding='utf8') as f:
    content = f.read()
    name = name_pattern.findall(content)[0]
    print(name)
f.close()