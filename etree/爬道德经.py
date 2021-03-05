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
    for a in range(1,82):#a表示1-81页的地址
        urls =f'https://www.daodejing.org/{a}.html' 
        di_list = requests.get(url=urls,headers=headers).text
        tree = etree.HTML(di_list)
        di2_list = tree.xpath('//*[@id="contain"]/div[4]')

        # if not os.path.exists('./meimei'):
        #         os.mkdir('./meimei')

    
        # open('道德经.txt','a',encoding='utf-8'):

        # 定义一个解决乱码的函数jiema
        def jiema (name):
            name = name.encode('iso-8859-1').decode('gbk')
            return name

        with open('道德经.csv','a',encoding='utf-8') as f:
            for li in di2_list:
                
                title = jiema(li.xpath('./p[1]/text()')[0])
                text1 = jiema(li.xpath('./p[2]/text()')[0])
                text2 = jiema(li.xpath('./p[5]/text()')[0])
                # text2 = li.xpath('./p[4]//text()')
                # text2 = text2.encode('iso-8859-1').decode('gbk')
                # text3 = jiema(li.xpath('./p[5]//text()'))
                # text4 = jiema(li.xpath('./p[11]//text()'))
                # text5 = jiema(li.xpath('./p[12]//text()'))


                print(title,text1,text2)
                
                f.write(title + '\n' + text1 + '\n'+ text2 + '\n')

    #         with open(img_path,'wb') as f:
    #             f.write(img_data)
    end_time = time.time()#设置结束时间
    print(end_time-start_time)#计算总耗时
