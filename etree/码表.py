# -*- coding: utf-8 -*-
import requests
from lxml import etree
import os
if __name__ == '__main__':

    headers = {
        'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36'
    }
    # url = 'https://m.78500.cn/kaijiang/p5/2021052.html'001-052，//*[@id="list"]/section[1]/section///a/h3/strong
    # f.open('./pai5.txt','w',encoding='utf-8')
    
    for i in range(1,53):#从第一期到第53期
        a = str(i).rjust(3,'0')
        urls =f'https://m.78500.cn/kaijiang/p5/2021{a}.html' 
        di_list = requests.get(url=urls,headers=headers).text
        tree = etree.HTML(di_list)
        di2_list = tree.xpath('/html/body/article')
        
        for i in di2_list:
            with open('pailie.txt','a',encoding='utf-8') as f:
                jiangqi = i.xpath('./div[1]/h1/strong/text()')[0]
                ma = i.xpath('./div[2]/span/i//text()')
                ma_dic = {
                    jiangqi : ma
                }
            
                dd = str(ma_dic)
                f.write(dd)
        

       

