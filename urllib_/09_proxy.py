import urllib.request

url = 'https://www.baidu.com/s?wd=ip'

headers = {
    'Bdpagetype': '3',
    'Bdqid': '0xc76980b1000f6eed',
    'Cache-Control': 'private',
    'Ckpacknum': '2',
    'Ckrndstr': '1000f6eed',
    'Connection': 'keep-alive',
    'Content-Encoding': 'br',
    'Content-Type': 'text/html;charset=utf-8',
    'Date': 'Sat, 23 Jul 2022 15:31:16 GMT',
    'Server': 'BWS/1.1',
    'Set-Cookie': 'delPer=0; path=/; domain=.baidu.com',
    'Set-Cookie': 'BD_CK_SAM=1;path=/',
    'Set-Cookie': 'PSINO=2; domain=.baidu.com; path=/',
    'Set-Cookie': 'BDSVRTM=28; path=/',
    'Set-Cookie': 'H_PS_PSSID=36548_36459_36255_36824_36454_36414_36668_36453_36165_36816_36885_36744_26350_36651; path=/; domain=.baidu.com',
    'Strict-Transport-Security': 'max-age=172800',
    'Traceid': '1658590276032572442614369157583800856301',
    'Transfer-Encoding': 'chunked',
    'Vary': 'Accept-Encoding',
    'X-Frame-Options': 'sameorigin',
    'X-Ua-Compatible': 'IE=Edge,chrome=1',
}

# ������̶��ip
proxies = {
    'http': '58.20.235.180:9091'
}

handler = urllib.request.ProxyHandler(proxies=proxies)

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf8')

with open('proxy.html', 'w', encoding='utf8') as fp:
    fp.write(content)
