import json
import urllib.request
from settings import headers

url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=40&limit=20'

request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)

content = response.read().decode('utf8')

# print(json.loads(content))

fp = open('douban.json', 'w', encoding='utf-8')

fp.write(content)
