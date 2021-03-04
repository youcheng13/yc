import requests
from lxml import etree
import time
import sys		#以下三行是为了解决编码报错问题
# # reload(sys)
# sys.setdefaultencoding("utf8")

fo = open("xiaoshuo.txt","w")
i=1
for i in range(5):
    url = "https://www.qidian.com/all?orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page=%d"%i
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
    data = requests.get(url,headers=header).text
    f = etree.HTML(data)

    hrefs = f.xpath('/html/body/div[1]/div[5]/div[2]/div[2]/div/ul/li/div[2]/h4/a/@href')
    for href in hrefs:
        href = "https:"+href
        book = requests.get(href,headers=header).text
        e = etree.HTML(book)    
        title = e.xpath('/html/body/div/div[6]/div[1]/div[2]/h1/em/text()')[0]
        zuozhe = e.xpath('/html/body/div/div[6]/div[1]/div[2]/h1/span/a/text()')[0]
        jieshao = e.xpath('/html/body/div/div[6]/div[4]/div[1]/div[1]/div[1]/p/text()')
        yuepiao = e.xpath('//*[@id="monthCount"]/text()')[0]
        str = '<----->'+title+'<----->'+zuozhe+'<----->'+yuepiao+'\n'
        fo.write(str)
        for te in jieshao:
            fo.write(te)

fo.close()
