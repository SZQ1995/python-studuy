"""
Python中，属性可以分为实例属性和类属性。

这个链接有详细介绍两者区别
https://www.cnblogs.com/scolia/p/5582268.html

"""


class Person(object):
    # 定义类属性
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # 对count类属性进行+1操作，用于记录这个Person类一共生成了多少个对象
        Person.count += 1
        #如果是下面这么操作 当先去实例对象中找 若没有 则去类属性中找
        print(self.count)
        # 这个操作相当于创建 该实例的属性 而不是修改类属性  有些类似 局部变量和全局变量
        self.count=3
        print(self.count)

p1 = Person('Tom', 23)
p2 = Person('Harry', 26)
print(f'我们共使用Person类生成了{Person.count}个实例对象')
print(p1.count)



"""
类方法
基本语法
@classmethod
def 类名称(cls):
    pass

类方法需要用修饰器@classmethod 来标识，告诉解释器这是一个类方法
类方法的第一个参数应该是cls,cls世界上跟self类似，有那个类调用方法，cls就指向哪个类的引用
通过cls.属性名 或者cls.方法名


为什么需要类方法，在面向对象中，特别强调数据封装性。
所以不建议直接在类的外部对属性进行直接设置和获取。
所以我们如果想操作类属性，建议使用类方法。
"""


class Tool():
    count = 0
    def __init__(self, name):
        self.name = name
        Tool.count += 1

    # 封裝一个类方法 专门实行对Tool.count类属性进行操作

    @classmethod
    def get_count(cls):
        print(f'我们使用Tool类共实例化了{cls.count}个工具')


t = Tool('斧头')
t.get_count()

"""
静态方法

基本语法
@staticmethod
def 方法名():
    pass

在开发时，如果需要在类中封装一个方法，这个方法：  
① 既 不需要访问实例属性或者调用实例方法
② 也 不需要访问类属性或者调用类方法
这个时候，可以把这个方法封装成一个静态方法
"""
class Game():

    @staticmethod
    def menu():
        print('1、开始游戏')
        print('2、游戏暂停')
        print('3、退出游戏')
Game.menu()