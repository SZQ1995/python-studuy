#元组可以存储多个数据且元组内的数据是不能修改的。
# 元组使用逗号 隔开数据



t1=(10,20,30)
print(type(t1))

# 若只有单个元素 则为单个元素的类型 不是元组
t2=(10)
print(type(t2))

print(t1[1])
print(len(t1))