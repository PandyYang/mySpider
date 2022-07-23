import random
import time
import urllib.request
import urllib.parse
from settings import headers
import os

url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=40&limit=20'


def create_request(page):
    base_url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'

    data = {
        'start': (page - 1) * 20,
        'limit': 20
    }

    data = urllib.parse.urlencode(data)
    full_url = base_url + data
    request = urllib.request.Request(url=full_url, headers=headers)

    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf8')

    return content


def download(page, content):
    dir = r'E:\PycharmProjects\mySpider\urllib_\douban'
    path = '\douban_' + str(page) + ".json"
    isExist = os.path.exists(dir)
    if not isExist:
        os.mkdir(dir)

    with open(dir + path, 'w', encoding='utf8') as fd:
        fd.write(content)


def random_sleep():
    ran = random.randrange(1, 3)
    time.sleep(ran)
    return ran


if __name__ == '__main__':
    start_page = int(input('please input the page start num:'))
    end_page = int(input('please input the page end num:'))

    for page in range(start_page, end_page + 1):
        request = create_request(page)
        content = get_content(request)
        download(page, content)
        seconds = random_sleep()
        print("====scrapy==page==" + str(page) + '======now======' + "sleep " + str(seconds) + "===sec==...")
