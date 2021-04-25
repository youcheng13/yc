from threading import Thread  #线程类

def func():
    for i in range(1000):
        print('子线程',i)


if __name__ == '__main__':
    t = Thread(target=func)  #创建线程并给线程安排任务
    t.start()  #多线程状态为可以开始工作，具体的执行时间由CPU决定
    for i in range(1000):
        print('主线程',i)