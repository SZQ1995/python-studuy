"""
变量 = lambda 函数参数:表达式（函数代码 return返回值）
# 调用变量
变量()
"""


# 编写一个函数求两个数的和
def fn1(num1, num2):
    return num1 + num2


print(fn1(10, 20))

# 替换成 lambda
fun2 = lambda num1, num2: num1 + num2
print(fun2(1, 2))

# 带默认参数的lambda表达式
fun3 = lambda num1, num2=12: num1 + num2

# 不定长参数：可变参数*args  接收的是一个元组
fun4 = lambda *args: args[1]
print(fun4(1, 2, 3, 4))

# 不定长参数：可变参数*args  接收的是一个字典
fun5 = lambda **args: args
print(fun5(name="tome", age=12))

# 带if判断的lambda表达式
fn = lambda a, b: a if a > b else b
print(fn(10, 20))

"""
列表数据+字典数据排序（重点）

知识点：列表.sort(key=排序的key索引, reverse=True)
"""
students = [
    {'name': 'Tom', 'age': 20},
    {'name': 'Rose', 'age': 19},
    {'name': 'Jack', 'age': 22}
]
#按照name值升序 reverse表示升序
students.sort(key=lambda  x:x['name'])
print(students)
students.sort(key=lambda  x:x['name'],reverse=True)
print(students)

#按照age值升序
students.sort(key=lambda x:x['age'])
print(students)