"""
把==函数作为参数传入==，这样的函数称为高阶函数，
高阶函数是函数式编程的体现。
函数式编程就是指这种高度抽象的编程范式。


① 正数的绝对值是它本身 ② 负数的绝对值是它的相反数
abs()返回的结果都是正数
abs(-10) # 10
`round()`函数可以完成对数字的四舍五入计算。
round(1.2)  # 1
round(1.9)  # 2

"""

# 需求：任意两个数字，按照指定要求（① 绝对值 ② 四舍五入）整理数字后再进行求和计算。
from functools import reduce


def fn1(num1, num2):
    return abs(num1) + abs(num2)
print(fn1(-10, 10))
def fn2(num1, num2):
    return round(num1) + round(num2)
print(fn2(10.2, 6.9))

# 要求：我们能不能对以上进行简化，然后合并为同一个函数 => 设计思想（高阶函数）
def fun3(num1,num2,f):
    return f(num1)+f(num2)
print(fun3(-10,10,abs))
print(fun3(10.2,6.9,round))

"""
map()函数

map(func, lst)`，将传入的函数变量func作用到lst变量的每个元素中，并将结果组成新的列表(Python2)/迭代器(Python3)返回。
lst = [1, 2, 3]
func函数：求某个数的平方，如输入2返回4，输入3返回9
map(func, lst)`返回结果[1, 4, 9]
"""

def funm(x):
    return x**2
list1=[1,2,3]
list2=list(map(funm,list1))
print(list2)

"""
reduce()函数

`reduce(func，lst)`，其中func必须有两个参数
。每次func计算的结果继续和序列的下一个元素做累加计算。
> 注意：reduce()传入的参数func必须接收2个参数。
"""
def funr(a,b):
    return a+b
list1=[1,2,3]
print(reduce(funr,list1))
# 若funr 是乘法 就是累乘

"""
filter()函数

filter(func, lst)函数用于过滤序列, 过滤掉不符合条件的元素,
 返回一个 filter 对象。如果要转换为列表, 可以使用 list() 来转换。
"""
# 定义一个函数（获取所有的偶数）
def func(n):
   return n % 2 == 0
# 定义一个序列
list1 = [1, 2, 3, 4, 5, 6, 7, 8]
# 调用filter函数进行过滤操作
result = filter(func, list1)
print(list(result))

