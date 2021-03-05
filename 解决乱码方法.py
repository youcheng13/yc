# 解决乱码的问题
#         1.在接收到response数据的时候，把它手动编码成"utf-8",因为Python默认就是"utf-8"格式
#         response.encoding = "utf-8"
#         2.对某个文字进行编码,这是一种较为通用的解决中文乱码的方案
#         name.encode("iso-8859-1").decode("gbk")

1.方法

response = requests.get(url=url,headers=headers)
    response.encoding = 'utf-8'
    page_text = response.text

2.方法

for li in li_list:
        title = li.xpath('./a/text()')
        title = title.encode('iso-8859-1').decode('gbk')