"""
多态指的是一类事物有多种形态。

定义：多态是一种使用对象的方式，子类重写父类方法，调用不同子类对象的相同父类方法，可以产生不同的执行结果。
① 多态依赖继承
② 子类方法必须要重写父类方法
> 首先定义一个父类，其可能拥有多个子类对象。当我们调用一个公共方法时，传递的对象不同，则返回的结果不同。

好处：调用灵活，有了多态，更容易编写出通用的代码，做出通用的编程，以适应需求的不断变化！
"""
class Fruit(object):
    # 公共方法
    def makejuice(self):
        print('i can make juice')

class Apple(Fruit):
    def makejuice(self):
        print('i can make apple juice')

class Banana(Fruit):
    def makejuice(self):
        print('i can make banana juice')

class Orange(Fruit):
    def makejuice(self):
        print('i can make orange juice')

class Peach(Fruit):
    def makejuice(self):
        print('i can make peach juice')


# 定义公共方法如service
def service(obj):
    obj.makejuice()

apple = Apple()
banana = Banana()
orange = Orange()

for i in (apple, banana, orange):
    service(i)