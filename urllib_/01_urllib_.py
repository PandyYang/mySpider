import urllib.request

# myURL = urlopen("https://www.runoob.com/")
# print(myURL.read())

url_image = "https://img0.baidu.com/it/u=695160816,3070592386&fm=253&fmt=auto&app=138&f=JPEG?w=710&h=473"

urllib.request.urlretrieve(url=url_image, filename="spider.jpg")
