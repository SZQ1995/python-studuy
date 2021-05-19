# 定义全局变量
info = 20

# 定义funcA函数
def funcA():
    #如果要对全局变量进行修改则必须使用global声明全局变量
    # 不然系统会认为 你又在函数内定义了一个info
    global info
    # 修改全局变量
    info=12


# 定义funcB函数
def funcB():
    # 共享全局作用域中的全局变量info
    print(info)

funcA()
funcB()