from threading import Thread  #线程类

class MyThread(Thread):
    def run(self):  #固定的，当线程被执行的时候，被执行的就是run()
        for i in range(1000):
            print('子线程',i)

    


if __name__ == '__main__':
    t = MyThread()
    t.start()  #开始线程

    for i in range(1000):
        print('主线程',i)