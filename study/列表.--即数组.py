#Python中的列表 即 Java中的数组


aList = ["aa", "bb", "cc"]
print(type(aList))
print(aList[0])

# 1、查找某个元素在列表中出现的位置（索引下标）
list1 = ['apple', 'banana', 'pineapple']
print(list1.index('apple'))  # 0
# print(list1.index('peach'))  # 报错
if "aa" in aList:
    print("aa存在列表中")

names = ['孙悟空', '唐僧', '猪八戒']
# 在列表的尾部追加一个元素"沙僧"
names.append('沙僧')
print(names)
#在
names.insert(2,"沙僧")#指定插入的位置
print(names)

#del 删除列表中下标为X的元素
del names[0]
print(names)

#pop() 删除指定下标的数据(默认为最后一个)，并返回该数据
print(names.pop(0))

#remove()移除列表中某个数据的第一个匹配项
names.remove("沙僧")
print(names)

#extend() 列表结尾追加数据，如果数据是一个序列，则将这个序列的数据逐一添加到列表
list1 = ['Tom', 'Rose', 'Jack']
# 1、使用extend方法追加元素"Jennify"
names.extend("Jennify")
print(names)

# 2、建议：使用extend方法两个列表进行合并
list2 = ['Hack', 'Jennify']
list1.extend(list2)

print(list1)


list1 = ['貂蝉', '大乔', '小乔', '八戒']
# 修改列表中的元素
list1[3] = '周瑜'
print(list1)

list2 = [1, 2, 3, 4, 5, 6]
list2.reverse()
print(list2)

list3 = [10, 50, 20, 30, 1]
list3.sort()  # 升序(从小到大)
# 或
# list3.sort(reverse=True)  # 降序(从大到小)
print(list3)

list4 = list3.copy()
print(list4)


# 遍历 两种方式
for i in list1:
    print(i)

i=0
while i<len(list1):
    print(list1[i])
    i+=1


"""
字符串：join()方法
作用：和split()方法正好相反，其主要功能是把序列拼接为字符串
字符串.join(数据序列)
"""
list1 = ['apple', 'banana', 'orange']
print('-'.join(list1))