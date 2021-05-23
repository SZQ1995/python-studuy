"""
魔术方法
在Python中，`__xxx__()`的函数叫做魔法方法，指的是具有特殊功能的函数。
魔术方法都有默认 只能是覆盖重写，使用对象时候 自动调用


提到魔术方法：① 这个方法在什么情况下被触发 ② 这个方法有什么实际的作用
`__init__()`：初始化方法或者称之为“构造函数”，在对象初始化时执行，其主要作用就是在对象初始化时，对对象进行初始化操作（如赋予属性）
`__str__()`：对象字符串方法，当我们在类的外部，使用print方法输出对象时被触发，其主要功能就是对对象进行打印输出操作，要求方法必须使用return返回字符串格式的数据。
`__del__()`：删除方法或者称之为“析构方法”，在对象被del删除时触发，其主要作用就是适用于关闭文件、关闭数据库连接等等。
"""


class Student():

    # 构造函数__init__
    def __init__(self, name, password):
        self.name = name
        self.password = password

    # __str__()方法
    """
    当使用print输出对象的时候，默认打印对象的内存地址。
    如果类定义了`__str__`方法，那么就会打印从在这个方法中 return 的数据
    """

    def __str__(self):
        return f"姓名：{self.name},密码：{self.password}\n"

    # 析构方法__del__
    # 实际应用是主要用于关闭文件操作、关闭数据库连接等等
    def __del__(self):
        print(f'{self}对象已经被删除')


s = Student("SZQ", 12)
print(s)

"""
单例模式
__new__()方法

使用类名()创建对象时，Python的解释器首先会调用`__new__方法`为对象分配空间。

__new__是一个由object积累提供的内置的静态方法，主要作用有两个：
○ 在内存中为对象分配空间
○ 返回对象的引用
Python解析器获得对象的引用后，将引用作为第一个参数，传递给`__init__方法`。重写`__new__方法`的代码非常固定，
一定要使用`return super().__new__(cls)`，否则Python解释器得不到分配了空间的对象引用，就不会调用对象的初始化方法。
`__new__方法`是一个静态方法，在调用时，要求将自身类信息cls作为参数传递到这个方法中，这个方法属于object类中的一个静态方法。
"""


# 如果不应用单例模式 如下面 代码 则会创建多个播放器，占据多个内存空间
# 定义一个播放器类
class MusicPlayer(object):
    def __init__(self, name):
        self.name = name

    # 默认的内置__new__方法
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)


# 1、实例mp1对象
mp1 = MusicPlayer('红色的高跟鞋')
print(mp1)

# 2、实例化mp2对象
mp2 = MusicPlayer('春夏秋冬')
print(mp2)


# 下面应用了单例模式

class MusicPlay2():
    # 定义一个类属性 用来记录实例化对象的个数
    # 注：类属性在内存中是一个特殊的存在，其不用于以前讲过的局部变量（局部变量当函数执行完毕后，其会被内存所销毁）。
    # 但是类属性一旦定义，除非对象以及这个类在内存中被销毁了，否则其不会自动销毁。
    instance = None

    def __init__(self, name):
        self.name = name

    # 重写__new__()方法
    def __new__(cls, *args, **kwargs):
        # 判断实例化时有没有分配过内存空间
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance


m1 = MusicPlay2('菊花开')
print(m1)
m2 = MusicPlay2('花前月下')
print(m2)

"""
__file__方法
见本项目自定义的random.py文件
用于输出模块的文件路径
"""

"""
__all__魔术方法

如果一个模块文件中有`__all__`变量，当使用`from xxx import *`导入时，只能导入这个列表中的元素。
主要功能：限制使用模块中的某些功能，也就是说你导入后可以使用的方法只能是`__all__`中封装好的方法。

案例
my_module.py
__all__ = ['func1']

def func1():
    print('func1方法')

def func2():
    print('func2方法')
    
限制引用模块中的方法.py
from my_module import *

func1()
func2()  # 报错 因为上面__all__中只有func1()
"""

"""
__dict__方法
将对象变成字典格式
"""
