import requests
import asyncio 
import time 
import aiohttp

start_time = time.time()
urls =[
    'http://www.baidu.com','http://www.sina.com','http://www.hao123.com'
]
async def get_page(url):
    async with aiohttp.ClientSession() as session:
        #get()、post():
        #headers,params/data,proxy='http://ip:port'
        async with await session.get(url) as response:
            #text()返回字符串形式的响应数据
            #read()返回二进制形式的响应数据
            #ison()返回的就是json对象
            #注意：获取响应数据操作之前一定要使用await进行手动挂起
            page_text = await response.text()
            print(page_text)
tasks = []

for url in urls:
    c = get_page(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end_time = time.time()
print('总耗时：',end_time-start_time)
      
