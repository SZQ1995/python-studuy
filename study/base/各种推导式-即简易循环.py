"""
基本语法：

```python
变量名 = [表达式 for 变量 in 列表 for 变量 in 列表]
变量名 = [表达式 for 变量 in 列表 if 条件]
```

案例：定义0-9之间的列表
list1 = []
for i in range(10):
    list1.append(i)
print(list1)
"""

# 列表推导式先运行表达式右边的内容：
# 当第一次遍历时：i = 0，其得到变量i的结果后，会放入最左侧的变量i中，这个时候列表中就是[0]
# 当第二次遍历时：i = 1，其得到变量i的结果后，会追加最左侧的变量i中，这个时候列表中就是[0, 1]
# ...
# 当最后一次遍历时：i = 9，其得到变量i的结果后，会追加最左侧的变量i中，这个时候列表中就是[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list1 = [i for i in range(10)]
print(list1)

"""
列表推导式 + if条件判断

变量 = [表达式 for 临时变量 in 序列 if 条件判断]

等价于
for 临时变量 in 序列:
    if 条件判断
    
"""

list1 = [i for i in range(10) if i % 2 != 0]
print(list1)

"""
for循环嵌套列表推导式

for 临时变量 in range(n):
    for 临时变量 in range(n):
    
基本语法：
变量 = [表达式 for 临时变量 in 序列 for 临时变量 in 序列]
"""

list1 = [(i, j) for i in range(4) for j in range(3)]
print(list1)

"""
字典推导式
基本语法：
① 字典推导式列表推导式思想的延续，语法差不多，只不过产生的是字典而已。
② 字典推导式格式：
变量 = {key:value for key,value in 序列}
"""

# 案例1：创建一个字典：字典key是1-5数字，value是这个数字的2次方。
dict1 = {i: i * 2 for i in range(8)}
print(dict1)

# 案例2：把两个列表合并为一个字典
list1 = ['name', 'age', 'gender']
list2 = ['Tom', 20, 'male']
# 结果：person = {'name':'Tom', 'age':20, 'gender':'male'}
person = {list1[i]: list2[i] for i in range(len(list1))}
print(person)

# 案例3：提取字典中目标数据
counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'ACER': 99}
# 需求：提取上述电脑数量大于等于200的字典数据
count={key:value for key,value in counts.items() if value>=200}
print(count)

"""
集合推导式
集合推导式跟列表推导式非常相似，唯一区别在于用 { } 代替 [ ]。
思考：为什么需要集合推导式，列表推导式不香么？
答：集合的最大特点就是去重
"""

list1 = [1, 1, 2]
set1 = {i**2 for i in list1}
print(set1)