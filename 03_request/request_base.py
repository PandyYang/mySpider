import requests

url = 'https://www.baidu.com'

response = requests.get(url)
print(type(response))

print(response.text)

print(response.url)

print(response.content)

print(response.status_code)

print(response.headers)