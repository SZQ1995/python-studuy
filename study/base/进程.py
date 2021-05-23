from multiprocessing import Process


def task1():
    while True:
        print('this is task1')

def task2():
    while True:
        print('this is task2')


# if __name__=='__main__':
#     process1 = Process(target=task1)
#     process1.start()
#     process2 = Process(target=task2)
#     process2.start()


"""
自定义进程
"""
class MyProcess(Process):

    def __init__(self,name):
        super(MyProcess,self).__init__()
        self.name=name

    #重写run方法
    def run(self):
        n=1
        while True:
            print('进程名字：'+self.name)
            print(f'------>自定义进程，{n}：{self.name}')
            n+=1

if __name__=='__main__':
    p1=MyProcess('小米')
    p1.start()
    p2=MyProcess('小红')
    p2.start()