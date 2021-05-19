def func():
    # 经过一系列操作返回一个元组
    return 100, 200	 # tuple元组类型的数据

# 定义两个变量接收元组中的每个数组（拆包）
num1, num2 = func()
# 打印num1和num2
print(num1)
print(num2)

"""
记住：字典拆包，只能把每个元素的key拆出来
"""
dict1 = {'name':'小明', 'age':18}
# 拆包的过程（字典）
a, b = dict1
print(a)
print(b)
# 获取字典中的数据
print(dict1[a])
print(dict1[b])

"""
通过拆包 实现两个数的交换

原理：

第一步：把c2和c1组成一个元组（c2，c1）
第二步：使用拆包特性，把元组中的两个元素分别赋值给c1和c2
"""
c1 = 10
c2 = 2
c1, c2 = c2, c1


"""
Python中数据的传递案例

需求：把元组传递给*args参数，字典传递给**kwargs
① 如果想把元组传递给*args，必须在tuple1的前面加一个*号
② 如果想把字典传递给**kwargs，必须在dict1的前面加两个**号
"""

def func(*args, **kwargs):
    print(args)
    print(kwargs)
# 定义一个元组（也可以是列表）
tuple1 = (10, 20, 30)
# 定义一个字典
dict1 = {'first': 40, 'second': 50, 'third': 60}
# 需求：把元组传递给*args参数，字典传递给**kwargs
# ① 如果想把元组传递给*args，必须在tuple1的前面加一个*号
# ② 如果想把字典传递给**kwargs，必须在dict1的前面加两个**号
func(tuple1,dict1) #这种是错误的
func(*tuple1,**dict1) #这种才是对的