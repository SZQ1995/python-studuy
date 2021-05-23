

# 集合（set）是一个无序的不重复元素序列
# 我们可以使用一对花括号{}或者set()方法来定义集合，
# 但是如果你定义的集合是一个空集合 ，则只能使用set()方法


# 定义一个集合
s1 = {10, 20, 30, 40, 50}
print(s1)
print(type(s1))

# 定义一个集合：集合中存在相同的数据 则去除重复
s2 = {'刘备', '曹操', '孙权', '曹操'}
print(s2)
print(type(s1))

# 定义空集合
s3 = {}
s4 = set()
print(type(s3))	 # <class 'dict'>
print(type(s4))  # <class 'set'>

# add()方法：向集合中增加一个元素（单一）
s5=set()
s5.add("hhahah")
print(s5)

# update()方法：向集合中增加序列类型的数据（字符串、列表、元组、字典）
list1={"a","b"}
s5.update(list1)
print(s5)

# 使用remove方法删除a这个元素  若没有a 则会报错
s5.remove("a")
# 使用discard方法删除未知元素  若未找到 不会报错
s5.discard("c")
# 随机删除一个元素
s5.pop()


# 求集合中的交集、并集、差集
s1 = {'刘备', '关羽', '张飞', '貂蝉'}
s2 = {'袁绍', '吕布', '曹操', '貂蝉'}

# 求交集
print(s1 & s2)
# 求并集
print(s1 | s2)
# 求差集
print((s1 - s2) | (s2 - s1))
