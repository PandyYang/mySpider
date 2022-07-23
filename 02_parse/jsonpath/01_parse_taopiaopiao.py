import urllib.request

import jsonpath
import json

url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1658598599742_55&jsoncallback=jsonp56&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'

headers = {
    # ':authority': 'dianying.taobao.com',
    # ':method': 'GET',
    # ':path': '/cityAction.json?activityId&_ksTS=1658598599742_55&jsoncallback=jsonp56&action=cityAction&n_s=new&event_submit_doGetAllRegion=true',
    # ':scheme': 'https',
    'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
    'bx-v': '2.2.0',
    'cookie': 't=0b04230be0e975d36447ba8e3873aa78; cookie2=1758ed300f1c3179d65f522233cce381; v=0; _tb_token_=f5e55077eee3e; cna=iBxXG2sYEz4CAXj0Hup35fjH; xlly_s=1; tb_city=110100; tb_cityName="sbG+qQ=="; tfstk=c_bPBvGDUzUPPuSN0ETUOefnL1TRZTBheqJ2qRsMJmY0ddKliCHpiLOJgLlqK3f..; l=eBPg7lvrLVr81ODABOfwhurza77OMIRAguPzaNbMiOCPO51p5vwPW6vpX589CnGVh6mJR3Wrj_IwBeYBq5vsjqj495I6MwMmn; isg=BDQ0YiOr6rt-5n53Sr6ZPfE4BfKmDVj3cYyfss6Vvr9COdSD9h2Vh7p3uXHhwZBP',
    'referer': 'https://dianying.taobao.com/cinemaList.htm?spm=a1z21.6646277.city.1.1aa161e1cJSpzr&n_s=new&city=110100',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

content = content.split('(')[1].split(')')[0]

# with open('taopp_.json', 'w', encoding='utf-8') as fp:
#     fp.write(content)

obj = json.load(open('taopp.json', 'r', encoding='utf8'))

data = jsonpath.jsonpath(obj, '$..regionName')
print(data)