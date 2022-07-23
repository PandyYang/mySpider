# 请求对象的定制

import urllib.request

from settings import headers

url = 'https://www.baidu.com'

# urlopen方法中不能存储字典 所以headers不能传递进去

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf8')

print(content)
