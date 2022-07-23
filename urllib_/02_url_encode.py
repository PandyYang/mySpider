import urllib.parse
import urllib.request

data = {
    'wd': '周杰伦',
    'sex': '男',
    'location': '台湾',
}

a = urllib.parse.urlencode(data)

base_url = 'https://www.baidu.com/s?'

data = {
    'wd': '周杰伦',
    'sex': '男',
    'location': '台湾省'
}

new_data = urllib.parse.urlencode(data)

print(new_data)

url = base_url + new_data

print(url)

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 "
                  "Safari/537.36 "
}

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

# 获取网页源码数据
content = response.read().decode('utf8')

print(content)
