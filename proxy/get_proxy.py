# encoding : utf-8
import random

import requests


def main():
    proxy_uri = requests.get('http://43.138.109.202:5000/fetch_all').text
    proxies = str(proxy_uri).split(",")
    http_proxies = list(filter(lambda x: x.find("http") != -1, proxies))
    if len(proxy_uri) == 0:
        print(u'暂时没有可用代理')
        return
    print(http_proxies)

    proxy = {'http': random.choice(http_proxies)}

    try:
        html = requests.get('http://www.baidu.com', proxies=proxy).text
        if u'百度一下，你就知道' in html:
            print('代理可用')
        else:
            print('代理不可用')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()