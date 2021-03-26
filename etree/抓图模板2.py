# -*- coding: utf-8 -*-
import requests
from lxml import etree
import os
import time
if __name__ == '__main__':

    headers = {
        'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36'
    }
    url = 'https://www.gdgusta.com/bgjjsccj.html'
    
    response = requests.get(url=url,headers=headers)
    response.encoding = 'utf8'
    a_text =response.text
    # di_list = requests.get(url=url,headers=headers).text
    tree = etree.HTML(a_text)
    di2_list = tree.xpath('//*[@id="category"]/div')
    # print(di2_list)

    if not os.path.exists('./办公'):
        os.mkdir('./办公')
    
    for li in di2_list:
        # img_src = ('./div/a/img/@src')
        # print(img_src)
        img_src = li.xpath('./div/a/img/@src')[0]
        img_name = li.xpath('./div/a/img/@title')[0]+'.jpg'
        # img_name = img_name.encode('iso-8859-1').decode('gbk')
        img_data = requests.get(url=img_src,headers=headers).content
        img_path = '办公/'+img_name

        with open(img_path,'wb') as f:
            f.write(img_data)
    
