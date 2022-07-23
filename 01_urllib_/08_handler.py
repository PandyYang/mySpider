# -*- coding: utf-8 -*-
# handler处理器的使用

# 需求 使用handler访问百度 获取网页源码

import urllib.request
from settings import headers

url = 'https://www.baidu.com'

request = urllib.request.Request(url=url, headers=headers)

# handler build_opener open

handler = urllib.request.HTTPHandler()
opener = urllib.request.build_opener(handler)
response = opener.open(request)

content = response.read().decode('utf8')
print(content)
