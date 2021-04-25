from multiprocessing import Process  #进程类

def func():
    for i in range(1000):
        print('子进程',i)


if __name__ == '__main__':
    p = Process(target=func)  #创建进程并给进程安排任务
    p.start()  #多进程状态为可以开始工作，具体的执行时间由CPU决定
    for i in range(1000):
        print('主进程',i)