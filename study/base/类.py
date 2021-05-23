"""
在Python中，我们可以有两种类的定义方式：
Python2（经典类）和 Python3（新式类）

类名不区分大小写，遵守一般的标识符的命名规则
（以字母、数字和下划线构成，并且不能以数字开头），
一般为了和方法名相区分，类名的首字母一般大写！（大驼峰法）
"""


# 经典类：不由任意内置类型派生出的类，称之为经典类
class old:
    # 属性
    # 方法
    pass


# 新式类：
class new():
    # 属性
    # 方法
    pass


# 举例
# 定义一个类
class Person():
    # 创建方法
    def eat(self):
        print("吃东西")
        # 一句话总结：类中的self就是谁实例化了对象，其就指向谁。
        self.see()

    def see(self):
        print("看东西")


# 创建一个对象
p = Person()
# 调用一个对象方法
p.eat()

"""
在类的外面添加属性和获取属性
对象名.属性 = 属性值
"""


# 1、定义一个Person类
class Person2():
    pass


# 2、实例化Person类，生成p1对象
p1 = Person2()
# 3、为p1对象添加属性
p1.name = '老王'
p1.age = 18
p1.address = '北京市顺义区京顺路99号'
print(f"你的姓名：{p1.name}，年龄{p1.age}")

"""
在类的内部获取外部定义的属性
"""


# 1、定义一个Person类
class Person2():
    def speak(self):
        print(f'我的名字：{self.name}，我的年龄：{self.age}，我的住址：{self.address}')


# 2、实例化Person类，生成p1对象
p2 = Person2()
# 3、添加属性
p2.name = '孙悟空'
p2.age = 500
p2.address = '花果山水帘洞'
# 4、调用speak方法
p2.speak()


"""
私有属性 
设置私有属性和私有方法的方式非常简单：在属性名和方法名 前面 加上两个下划线 `__` 即可。

类中的私有属性和私有方法，不能被其子类继承

在Python中，
定义函数名' get_xx '用来获取私有属性，
定义' set_xx '用来修改私有属性值。
"""


class Teacher():

    def __init__(self, name, age=12):
        # 定义公有属性 name
        self.name = name
        # 定义私有属性 password
        self.__age = age

    # 公共方法：提供给外部的访问接口
    def get_age(self):
        return self.__age

    # 公共方法：提供给外部的设置接口
    def set_age(self, age):
        self.__age = age

t=Teacher('XYR')
t.set_age(23)
print(t.get_age())