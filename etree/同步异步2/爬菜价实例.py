import requests
from lxml import etree
import csv
import time
from concurrent.futures import ThreadPoolExecutor

start_time = time.time()

f = open("data.csv",mode="w",encoding="utf-8")
csvwriter = csv.writer(f)

def download_one_page(url):
    #拿到源代码
    resp = requests.get(url)
    html = etree.HTML(resp.text)
    table = html.xpath("/html/body/div[2]/div[4]/div[1]/table")[0]
    # trs = table.xpath("./tr")[1:] /和下面是一样效果的
    trs = table.xpath("./tr[position()>1]")
    # 拿到每个tr
    for tr in trs:
        txt = tr.xpath("./td/text()")
        # 对数据进行处理：\\ / 去掉
        txt = (item.replace('\\','').replace('/','') for item in txt)
        # 把数据存进文件中
        csvwriter.writerow(txt)
    print(url,'提取完毕')

if __name__ == '__main__':
    # for i in range(1,20000):  #效率低下，我们要用线程池
    #     download_one_page(f'http://www.xinfadi.com.cn/marketanalysis/0/list/{i}.shtml')

    with ThreadPoolExecutor(100) as t:  #建立一个50个线程的线程池
        for i in range(1,97928):
            t.submit(download_one_page,f'http://www.xinfadi.com.cn/marketanalysis/0/list/{i}.shtml')
    print("全部下载完成！")

    end_time = time.time()

print(end_time-start_time)


    