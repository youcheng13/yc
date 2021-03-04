import requests
import os
from lxml import etree
if __name__ == "__main__":
    url = "https://apis.baidu.com/store/aladdin/land?cardType=ipSearch"
    headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:84.0) Gecko/20100101 Firefox/84.0"
        }
        # 使用代理服务器进行requests访问
    response = requests.get(url=url,headers=headers)
    # 测试请求状态是否成功，返回200成功，返回300，400不成功
    print(response.status_code)
    page_text = response.text
    with open('ip.html','w',encoding='utf-8') as fp:
        fp.write(page_text)
    