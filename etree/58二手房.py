# -*- coding: utf-8 -*-
import requests
from lxml import etree
if __name__ == '__main__':

    headers = {
        'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36'
    }
    url = 'https://haikou.58.com/ershoufang/?PGTID=0d100000-0080-5a24-77d5-857687302b5f&ClickID=4'
    page_text = requests.get(url=url,headers=headers).text
    # print(page_text)
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//*[@id="__layout"]/div/section/section[3]/section[1]/section[2]/div')

    with open('58.txt','w',encoding='utf-8') as f:
        for li in li_list:
            title = li.xpath('./a/div[2]/div/div/h3/text()')[0]
            jiage = li.xpath('./a/div[2]/div[2]/p[1]/span/text()')[0]
            pingfang = li.xpath('./a/div[2]/div/section/div/p[2]/text()')[0]

            # print(title)
            f.write(title+':'+jiage+'万'+pingfang+'\n')