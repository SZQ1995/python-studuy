"""
多线程
Python3 线程中常用的两个模块为：
_thread
threading(推荐使用)
thread 模块已被废弃。用户可以使用 threading 模块代替。
所以，在 Python3 中不能再使用"thread" 模块。为了兼容性，Python3 将 thread 重命名为 "_thread"。

"""
import threading
from time import sleep, ctime, time


def download(n):
    images=['girl.jpg','man.jpg','boy.jpg']
    for img in images:
        print('正在下载:',img)
        sleep(n)
        print('下载成功:',img)

# if __name__=='__main__':
#     thread = threading.Thread(target=download, args=(2,))
#     thread.start()
#     n=1
#     while True:
#         print(n)
#         sleep(1.5)
#         n+=1


"""
自定义线程
"""
exitFlag = 0
class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        #调用父类初始化方法
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print ("开始线程：" + self.name)
        print_time(self.name, self.counter, 5)
        print ("退出线程：" + self.name)

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        sleep(delay)
        print ("%s: %s" % (threadName, ctime(time())))
        counter -= 1

# if __name__ == '__main__':
#     # 创建新线程
#     thread1 = myThread(1, "Thread-1", 1)
#     thread2 = myThread(2, "Thread-2", 2)
#
#     # 开启新线程
#     thread1.start()
#     thread2.start()
#     #join()阻塞主线程 等待子线程执行完毕
#     thread1.join()
#     thread2.join()
#     print ("退出主线程")


"""
线程同步---利用锁
"""
threadLock = threading.Lock()
threads = []

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print ("开启线程： " + self.name)
        # 获取锁，用于线程同步
        threadLock.acquire()
        print_time(self.name, self.counter, 3)
        # 释放锁，开启下一个线程
        threadLock.release()

def print_time(threadName, delay, counter):
    while counter:
        sleep(delay)
        print ("%s: %s" % (threadName, ctime(time())))
        counter -= 1

if __name__ == '__main__':
    # 创建新线程
    thread1 = myThread(1, "Thread-1", 1)
    thread2 = myThread(2, "Thread-2", 2)

    # 开启新线程
    thread1.start()
    thread2.start()

    # 添加线程到线程列表
    threads.append(thread1)
    threads.append(thread2)

    # 等待所有线程完成
    for t in threads:
        t.join()
    print ("退出主线程")
