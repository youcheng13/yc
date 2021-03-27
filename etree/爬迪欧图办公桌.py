# -*- coding: utf-8 -*-
import requests
from lxml import etree
import os
import time
if __name__ == '__main__':

    headers = {
        'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36'
    }
    for a in range(1,6):

        url = f'https://www.dious-f.com/bgzy-{a}.html'
        response = requests.get(url=url,headers=headers)
        response.encoding = 'utf8'
        AA_text =response.text
        # di_list = requests.get(url=url,headers=headers).text
        tree = etree.HTML(AA_text)
        di2_list = tree.xpath('/html/body/div[4]/div[1]/div[2]/dl')
        # print(di2_list)

        if not os.path.exists('/Volumes/MY/办公桌'):
            os.mkdir('/Volumes/MY/办公桌')
        
        for li in di2_list:
            img_src = "https://www.dious-f.com"+li.xpath('./dt/a/@href')[0]
            # print(img_src)
            response = requests.get(url=img_src,headers=headers)
            response.encoding = 'utf8'
            BB_text = response.text
            # print(BB_text)
            kk = etree.HTML(BB_text)
            kk_list = kk.xpath('//*[@id="printableview"]/div[7]')
            # print(kk_list)
            for nn in kk_list:
                tu_data = 'https://www.dious-f.com/'+ nn.xpath('./p/img/@src')[0]
                img_name = nn.xpath('./p/img/@title')[0]+'.jpg'
            # img_name = img_name.encode('iso-8859-1').decode('gbk')
                img_data = requests.get(url=tu_data,headers=headers).content
                img_path = '/Volumes/MY/办公桌/'+img_name

                with open(img_path,'wb') as f:
                    f.write(img_data)
    
