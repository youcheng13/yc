from multiprocessing import Process  #进程类

class MyProcess(Process):
    def run(self):  #固定的，当进程被执行的时候，被执行的就是run()
        for i in range(1000):
            print('子进程',i)

    


if __name__ == '__main__':
    p = MyProcess()
    p.start()  #开始进程

    for i in range(1000):
        print('主进程',i)