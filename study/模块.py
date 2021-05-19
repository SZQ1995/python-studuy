"""
Python 模块(Module)，是一个Python 文件，
以.py 结尾，包含了 Python 对象定义和Python语句。
模块能定义函数，类和变量，模块里也能包含可执行的代码。

在Python中，模块通常可以分为两大类：
内置模块(目前使用的) 和 自定义模块

基本语法：
import 模块名称
或
import 模块名称1, 模块名称2, ...


导入方式
☆ import 模块名
☆ from 模块名 import 功能名
☆ from 模块名 import *
☆ import 模块名 as 别名
☆ from 模块名 import 功能名 as 别名
"""

# 使用import导入math模块
import math

print(math.sqrt(9))

# 使用import导入math与random模块

print(random.randint(0, 5))

# 使用from 模块名 import 功能名
from math import sqrt

print(sqrt(6))

# 使用as关键字为导入模块定义别名
import time as t

t.sleep(1)
print(t.time())

# 导入自定义模块
from study import 类 as cl

c = cl.Person()
c.eat()

# 自定义模块中功能测试
# 引入一个魔方方法：`__name__`，其保存的内存就是一个字符串类型的数据。
# 随着运行页面的不同，其返回结果也是不同的：
# ① 如果`__name__`是在当前页面运行时，其返回结果为`__main__`
# ② 如果`__name__`在第三方页面导入运行时，其返回结果为模块名称

# 基于以上特性，我们可以把`__name__`编写在自定义模块中，其语法如下：
if __name__ == '__main__':
    # 执行测试代码
    print('当前是在当前类运行')


# `__name__`魔术方法除了可以在自定义模块中测试使用，还可以用于编写程序的入口：
# 定义一个main方法（入口文件）
def main():
    print('主程序运行')
    pass
# 执行我们要执行的功能
# ① 打印选择菜单
# ② 添加学员信息
# ③ 删除学员信息
# 调用执行入口
if __name__ == '__main__':
    main()

# 多模块中功能命名冲突问题
#  命名冲突
### 解决方案

# ① 把所有模块的导入方式都写入文件的最上面，如果发现命名冲突了，马上和模块的开发人员进行功能核对
# ② 给重名的方法进行as重命名