#字典 ---可以理解成Java中的Map key-value形式存储


# 有数据字典
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}

# 空字典
dict2 = {}
# 或者 dict定义空字典
dict3 = dict()



# 1、定义一个空字典
person={}
# 2、向字典中添加数据
person['name']="刘备"
person['age']=43
person['address']="四川蜀中"
# 3、使用print方法打印person字典
# print(person)

# del person['age']
# print(person)

# print(person['name'])
# print(person.get("name","没找到的默认值"))


# print(type(person.keys()))

# items()以列表返回可遍历的(键, 值) 元组数组
for i in  person.items():
    print(i[1])
#结合for循环对字典中的数据进行遍历
for key, value in person.items():
    print(f'{key}：{value}')


# person.clear()
# print(person)

# 开发通讯录管理系统
# 存储同学的信息（姓名，年龄，电话）
students=[]
# for i in range(2):
#     student = {}
#     student["name"]=input("请输入姓名：")
#     student["age"]=input("请输入年龄：")
#     student["phone"]=input("请输入电话：")
#     students.append(student)
# print(students)


"""
其实字典中的key可以是很多数据类型（
不可变数据类型 => 整型、浮点型、字符串、元组）
"""
my_dict = {}
my_dict = {}
my_dict[1] = 1  #my_dict={1:1}
my_dict['1'] = 2 #my_dict={1:1，'1':2}
my_dict[1.0] = 3 #my_dict={1:3，'1':2}
# 即 字典中 浮点型还是整型 只要相等 默认当做一个相同
print(my_dict[1] + my_dict['1'] + my_dict[1.0])
