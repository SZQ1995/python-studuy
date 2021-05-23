# | **运算符**  | **描述**        | **支持的容器类型**       |
# | ---------- | -------------- | ------------------------ |
# | +          | 合并            | 字符串、列表、元组       |
# | *          | 复制           | 字符串、列表、元组       |
# | in         | 元素是否存在   | 字符串、列表、元组、字典 |
# | not  in    | 元素是否不存在 | 字符串、列表、元组、字典 |

str1 = "hello"
str2 = "world"
print(str1 + str2)

list1 = ['a']
list2 = ['b']
print(list1 + list2)

tupple1 = (1, 1)
tupple2 = (2, 2)
print(tupple1 + tupple2)  # (1, 1, 2, 2)

# 1、字符串与乘号的关系
print('-' * 40)

# 2、列表与乘号的关系
list1 = ['*']
print(list1 * 10)  # ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']

# 3、元组与乘号的关系
tuple1 = (10,)
print(tuple1 * 10)

"""
**函数**                 | **描述**                              
 ------------------------ | ----------------------------------------
len()                    | 计算容器中元素个数                          
del或del()               | 根据索引下标删除指定元素                  
max()                    | 返回容器中元素最大值                      
min()                    | 返回容器中元素最小值                         
range(start,  end, step) | 生成从start到end（不包含）的数字，步长为  step，供for循环使用 |
enumerate()              | 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在  for  循环当中。 |
"""


# 定义一个字符串
str1 = 'hello world'
print(f'字符串的长度为{len(str1)}')

# 定义一个列表
list1 = [10, 20, 30, 40, 50]
print(f'列表的长度为{len(list1)}')

# 定义一个字典
dict1 = {'name':'哆啦A梦', 'gender':'male', 'address':'东京'}
print(f'字典的长度为{len(dict1)}')

# 定义一个列表
list1 = ['吕布', '董卓', '貂蝉']
# 使用del方法删除董卓
del list1[1]
print(list1)


# 定义一个字典
dict1 = {'name':'白龙马', 'age':23, 'address':'东海龙宫'}
# 使用del方法删除age
del dict1['age']
print(dict1)

list1 = [10, 20, 30, 40, 50]
n = 1
for i in list1:
    print(f'第{n}个数：{i}')
    n += 1

print('-' * 40)

for key, value in enumerate(list1):
    print(f'第{key+1}个数：{value}')


# 序列类型之间的相互转换

# list()方法：把某个序列类型的数据转化为列表
# 1、定义元组类型的序列
tuple1 = (10, 20, 30)
print(list(tuple1))
# 2、定义一个集合类型的序列
set1 = {'a', 'b', 'c', 'd'}
print(list(set1))
# 3、定义一个字典  转换 只会保留key  value部分直接被忽略
dict1 = {'name':'刘备', 'age':18, 'address':'蜀中'}
print(list(dict1))  #['name', 'age', 'address']

#tuple()方法：把某个序列类型的数据转化为元组
# 定义一个列表类型的数据
list1 = ['a', 'b', 'c', 'd']
print(tuple(list1))
# 定义一个集合类型的数据
set1 = {10, 20, 30, 40}
print(tuple(set1))

#set()方法：将某个序列转换成集合
# （但是要注意两件事 => ① 集合可以快速完成列表去重 ② 集合不支持下标）
# 定义一个列表类型的数据
list1 = ['a', 'b', 'c', 'd', 'a']
print(set(list1))
# 定义一个元组类型的数据
tuple1 = (10, 20, 30, 40)
print(set(tuple1))


