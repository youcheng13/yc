
import requests
import os
from lxml import etree
if __name__ == "__main__":
    url = "https://www.qidian.com/search?kw=python"
    headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:84.0) Gecko/20100101 Firefox/84.0"
	
        }
    r = requests.get(url=url,headers=headers)
    # 测试请求状态是否成功，返回200成功，返回300，400不成功
    print(r.status_code)
    page_text = r.text
    tree = etree.HTML(page_text)
    zi = tree.xpath('/html/body/div[1]/div[3]/div[1]/div[1]/ul/li[5]/dl/dd/a[2]/cite/text()')[0]
    print("起点排行免费书的数量："+zi)
   
   

