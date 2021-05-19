from study import random

"""
函数的作用有两个：
① 模块化编程
② 代码重用

基本语法：
def 函数名称([参数1, 参数2, ...]):

函数必须先定义后使用
"""


def myFirstFunction(a, b, c):
    print("myFirstFunction执行了")
    print(a, b, c)
    return 0


a = myFirstFunction('a', 8888, '666')
print(a)

"""
如果一个函数要有多个返回值，该如何书写代码？
答：在Python中，理论上一个函数只能返回一个结果。
但是如果我们向让一个函数可以同时返回多个结果，我们可以使用`return 元组`的形式。
"""


def return_num():
    return 1, 2


result = return_num()
print(result)
print(type(result))  # <class 'tuple'>


# 函数说明文档 说明需在方法体内部
# pass 是空语句 是占位符 不做任何操作
def add_student():
    """ 函数的说明文档：add_student方法不需要传递任何参数，其功能就是实现对通讯录的增加操作 """
    pass


# 可以通过 help(函数名)查看函数的说明文档


def generate_code():
    """生成4位数的验证码"""
    code = "";
    for i in range(4):
        code += str(random.randint(0, 9))
    return code


print(generate_code())


def reverse_str(str):
    str=str[::-1]#切片方式翻转
    return  str

print(reverse_str("abcdefg"))