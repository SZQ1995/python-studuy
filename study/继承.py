"""
所有类都是Object类的子类 这是默认的 可以不写
Object类是顶级类

Python中支持单继承和多继承
"""

# 假设A类要继承B类中的所有属性和方法（私有属性和私有方法除外）
class B(object):
    pass

class A(B):
    pass
a = A()



"""
单继承，具有传递性
如A类继承了B类，B类又继承了C类。则根据继承的传递性，则A类也会自动继承C类中所有属性和方法（公共
"""
# 定义父类
class Person(object):
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address

    def eat(self):
        print("i can eat food")

    def __str__(self):
        return f"姓名：{self.name} 年龄：{self.age}  地址:{self.address}"

# 定义Person的子类 Student
class Student(Person):
    pass


# 定义Student的子类 Child
class Child (Student):
    pass

s=Student('学生',12,'福州')
s.eat()
print(s)
c=Child('孩子',12,'福州')
c.eat()
print(c)


"""
多继承
"""
class B(object):
    pass

class C(object):
    pass

class A(B, C):
    pass
# a.B中的所有属性和方法
# a.C中的所有属性和方法
a = A()

# 具体实例
class GasolineCar(object):
    def run_with_gasoline(self):
        print('i can run with gasoline')


class EletricCar(object):
    def run_with_eletric(self):
        print('i can run with eletric')


class HybridCar(GasolineCar, EletricCar):
    pass


tesla = HybridCar()
tesla.run_with_gasoline()
tesla.run_with_eletric()

"""
继承的重写 重写也叫作覆盖
例如下面 Dog、Cat子类重写父类Animal中的call方法：
"""

class Animal(object):
    def eat(self):
        print('i can eat')
    # 公共方法
    def call(self):
        print('i can call')


class Dog(Animal):
    # 重写父类的call方法
    def call(self):
        print('i can wang wang wang')


class Cat(Animal):
    # 重写父类的call方法
    def call(self):
        print('i can miao miao miao')


wangcai = Dog()
wangcai.eat()
wangcai.call()

miaomiao = Cat()
miaomiao.eat()
miaomiao.call()

"""
super()调用父类属性和方法

super()：调用父类属性或方法，完整写法：`super(当前类名, self).属性或方法()`，
在Python3以后版本中，调用父类的属性和方法我们只需要使用`super().属性或super().方法名()`就可以完成调用了。
"""

# 代码略

"""
MRO属性或MRO方法：方法解析顺序
MRO(Method Resolution Order)：方法解析顺序，我们可以通过`类名.__mro__`或`类名.mro()`获得“类的层次结构”，
方法解析顺序也是按照这个“类的层次结构”寻找到。
"""


class Car(object):
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def run(self):
        print('i can run')


class GasolineCar(Car):
    def __init__(self, brand, model, color):
        super().__init__(brand, model, color)

    def run(self):
        print('i can run with gasoline')


class ElectricCar(Car):
    def __init__(self, brand, model, color):
        super().__init__(brand, model, color)
        # 电池属性
        self.battery = 70

    def run(self):
        print(f'i can run with electric，remain:{self.battery}')


print(ElectricCar.__mro__) #(<class '__main__.ElectricCar'>, <class '__main__.Car'>, <class 'object'>)
print(ElectricCar.mro())#[<class '__main__.ElectricCar'>, <class '__main__.Car'>, <class 'object'>]


# 说明：有MRO方法解析顺序可知，
# 在类的继承中，当某个类创建了一个对象时，调用属性或方法，
# 首先在自身类中去寻找，如找到，则直接使用，停止后续的查找。
# 如果未找到，继续向上一级继承的类中去寻找，
# 如找到，则直接使用，没有找到则继续向上寻找...直到object类，
# 这就是Python类继承中，其方法解析顺序。


