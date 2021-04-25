import requests
from lxml import etree
import os
import time

url = 'https://haikou.zbj.com/search/f/?type=new&kw=%E5%BE%AE%E4%BF%A1%E5%B0%8F%E7%A8%8B%E5%BA%8F'
headers = {
        'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36'
    }
response =requests.get(url=url,headers=headers).text
resp = etree.HTML(response)
# print(resp)
divs = resp.xpath('/html/body/div[6]/div/div/div[3]/div[6]/div[1]/div')

# if not os.path.exists('/Volumes/MY/公司'):
#     os.mkdir('/Volumes/MY/公司')
# print(divs)
for div in divs:
    price = div.xpath('./div[1]/div[1]/a[1]/div[2]/div[1]/span[1]/text()')[0].strip('¥')+'元'
    chengj = div.xpath('./div[1]/div[1]/a[1]/div[2]/div[1]/span[2]/text()')[0]
    name = div.xpath('./div[1]/div[1]/a[2]/div[1]/p/text()')[0]
    print(price)
    print(chengj)
    print(name)
