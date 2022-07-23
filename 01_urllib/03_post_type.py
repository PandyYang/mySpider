# post请求方式
import json
import urllib.request
import urllib.parse

url = 'https://fanyi.baidu.com/sug'

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 "
                  "Safari/537.36 "
}

data = {
    'kw': 'spider'
}

# post请求的参数 必须进行编码
# data = urllib.02_parse.urlencode(data)
data = urllib.parse.urlencode(data).encode('utf8')

print(data)

# post请求参数不会拼接到url后面，放在请求对象的定制对象中
request = urllib.request.Request(url=url, headers=headers, data=data)

print(request)

response = urllib.request.urlopen(request)

print(response)

content = response.read().decode('utf8')

print(content)

print(type(content))

print(json.loads(content))
