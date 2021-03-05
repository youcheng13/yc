import time
#导入线程池模块对应的类
from multiprocessing.dummy import Pool

start_time = time.time()
list = []
for a in range(2,5):
    urls =f'http://pic.netbian.com/4kmeinv/index_{a}.html' 
    list.append(urls)
print(list)



def get_page(str):
    response = requests.get(url=list)

# name_list =['xiazai','aa','bb','cc']
#实例化一个线程池对象
pool = Pool(4)
#将列表中每个列表元素传递给ge_page进行处理
pool.map(list)

end_time = time.time()
print(end_time-start_time)