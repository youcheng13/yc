# -*- coding: utf-8 -*-
import requests
from lxml import etree
import os
import time
if __name__ == '__main__':

    headers = {
        'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36'
    }
    url = 'https://www.dious-f.com/smbgj-1.html'
    
    response = requests.get(url=url,headers=headers)
    response.encoding = 'utf8'
    a_text =response.text
    # di_list = requests.get(url=url,headers=headers).text
    tree = etree.HTML(a_text)
    di2_list = tree.xpath('/html/body/div[4]/div[1]/div[2]/dl')
    print(di2_list)

    if not os.path.exists('./实木'):
        os.mkdir('./实木')
    
    for li in di2_list:
        img_src = li.xpath('./dt/a/@href')[0]
        print(img_src)
        ff = requests.get(url=img_src,headers=headers).text
        kk = tree.xpath('//*[@id="detailvalue0"]')
        print(kk)
        # for nn in kk:
        #     tu_data = nn.xpath('./p[1]/img/@src')[0]
        #     img_name = nn.xpath('./p[1]/img/@title')[0]+'.jpg'
        # # img_name = img_name.encode('iso-8859-1').decode('gbk')
        #     img_data = requests.get(url=tu_data,headers=headers).content
        #     img_path = '/实木'+img_name

        #     with open(img_path,'wb') as f:
        #         f.write(img_data)
    
