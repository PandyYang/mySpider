from lxml import etree
import urllib.request
import sys
from settings import headers

# 1.获取网页源码
# 2.解析 解析服务器响应的文件 etree.HTML

url = 'https://www.baidu.com'

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

# 获取网页源码
content = response.read().decode('utf8')
# print(content)

# 解析服务器响应的文件
tree = etree.HTML(content)

# 获取想要的数据
result = tree.xpath('//input[@id="su"]/@value')[0]
print(result)
