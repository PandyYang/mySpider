# Scrapy
## 1.创建scrapy 项目
```shell
scrapy startproject mySpider
```

### 2.项目组成
```shell
spiders
__init__.py
自定义的爬虫文件.py ‐‐‐》由我们自己创建，是实现爬虫核心功能的文件
__init__.py
items.py ‐‐‐》定义数据结构的地方，是一个继承自scrapy.Item的类
middlewares.py ‐‐‐》中间件 代理
pipelines.py ‐‐‐》管道文件，里面只有一个类，用于处理下载数据的后续处理
默认是300优先级，值越小优先级越高（1‐1000）
settings.py ‐‐‐》配置文件 比如：是否遵守robots协议，User‐Agent定义等
```

### 3.创建爬虫文件
（1）跳转到spiders文件夹 cd 目录名字/目录名字/spiders
（2）scrapy genspider 爬虫名字 待爬取的网页的域名

### 4. 爬虫的基本组成
```shell
name = 'baidu' ‐‐‐》 运行爬虫文件时使用的名字
allowed_domains ‐‐‐》 爬虫允许的域名，在爬取的时候，如果不是此域名之下的url，会被过滤掉
start_urls ‐‐‐》 声明了爬虫的起始地址，可以写多个url，一般是一个
parse(self, response) ‐‐‐》解析数据的回调函数
response.text ‐‐‐》响应的是字符串
response.body ‐‐‐》响应的是二进制文件
response.xpath()‐》xpath方法的返回值类型是selector列表
extract() ‐‐‐》提取的是selector对象的是data
extract_first() ‐‐‐》提取的是selector列表中的第一个数据
```

### 5.运行爬虫文件
```shell
scrapy crawl 爬虫名称
```