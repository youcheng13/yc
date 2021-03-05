# -*- coding: utf-8 -*-
import requests
from lxml import etree
import os
import time
if __name__ == '__main__':

    headers = {
        'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36'
    }
    # url = 'http://pic.netbian.com/4kmeinv/index_%d.html'
    start_time = time.time()#设置开始时间
    for a in range(2,5):#a表示2-5页的图片地址
        urls =f'http://pic.netbian.com/4kmeinv/index_{a}.html' 
        di_list = requests.get(url=urls,headers=headers).text
        tree = etree.HTML(di_list)
        di2_list = tree.xpath('//*[@id="main"]/div[3]/ul/li')

        if not os.path.exists('./meimei'):
                os.mkdir('./meimei')
    
        for li in di2_list:
            img_src = 'http://pic.netbian.com/'+li.xpath('./a/img/@src')[0]
            print(img_src)
            img_name = li.xpath('./a/img/@alt')[0]+'.jpg'
            img_name = img_name.encode('iso-8859-1').decode('gbk')
            img_data = requests.get(url=img_src,headers=headers).content
            img_path = 'meimei/'+img_name

            with open(img_path,'wb') as f:
                f.write(img_data)
    end_time = time.time()#设置结束时间
    print(end_time-start_time)#计算总耗时
