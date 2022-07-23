import random

proxies_poll = [
    {
        'http': '118.163.120.181:58837'
    },
    {
        'http': '61.160.236.33:3129'
    }
]

proxies = random.choice(proxies_poll)

print(proxies)
