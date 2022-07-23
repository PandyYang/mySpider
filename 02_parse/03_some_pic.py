import random
import time
import urllib.request
import urllib.parse
from settings import headers
import os
from lxml import etree


def create_request(page):

    if(page == 1):
        url = 'https://sc.chinaz.com/tupian/rentiyishu.html'
    else:
        url = 'https://sc.chinaz.com/tupian/rentiyishu_' + str(page) + '.html'

    request = urllib.request.Request(url=url, headers=headers)

    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf8')

    return content


def download(page, content):
    dir = r'E:\PycharmProjects\mySpider\02_parse\chinaz'
    path = '\chinaz_' + str(page) + ".json"
    isExist = os.path.exists(dir)
    if not isExist:
        os.mkdir(dir)

    tree = etree.HTML(content)
    name_list = tree.xpath('//div[@id="container"]//a/img/@alt')
    # for name in name_list:
    #     print(name)
    # print(len(name_list))

    src_list = tree.xpath('//div[@id="container"]//a/img/@src')
    # for src in src_list:
    #     print(src)
    # print(len(src_list))

    for i in range(len(name_list)):
        name = name_list[i]
        src = src_list[i]
        url = 'https:' + src
        # 获取原图
        url = url.replace('_s', '')
        print(name, url)

        urllib.request.urlretrieve(url, filename=dir + '\\' + name + '.jpg')

    # with open(dir + path, 'w', encoding='utf8') as fd:
    #     fd.write(content)


def random_sleep():
    ran = random.randrange(1, 3)
    time.sleep(ran)
    return ran

# 爬取一小时 完事一分钟 睡觉~~
if __name__ == '__main__':
    start_page = int(input('please input the page start num:'))
    end_page = int(input('please input the page end num:'))

    for page in range(start_page, end_page + 1):
        request = create_request(page)
        content = get_content(request)
        download(page, content)
        seconds = random_sleep()
        print("====scrapy==page==" + str(page) + '======now======' + "sleep " + str(seconds) + "===sec==...")
