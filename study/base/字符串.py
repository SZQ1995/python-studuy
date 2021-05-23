str = "this is " \
      "string"

"""
三个引号若是复制给一个变量则是字符串 否则为注释
三引号定义的字符串支持换行 无需添加\
例如下面
"""
str2 = """
    this is strinf
    hhhh
"""

# i=0
# while i<str.__le__():
#     print(str[i])
#     i+=1;


# 如果一定要在单引号中在放入一个单引号，必须使用反斜杠\进行转义。
# 注：在Python中，如果存在多个引号，
# 建议① 单引号放在双引号中 ② 双引号放在单引号中。
str3=" I'm tom"
str4=' I\'m tom'


# # 格式化的几种方式
# #百分号（Python2和Python3）
# name = input('请输入您的姓名：')
# age = int(input('请输入您的年龄：'))
# address = input('请输入您的住址：')
#
# print('我的名字是%s，今年%d岁了，家里住在%s...' % (name, age, address))
#
# # format方法（Python3）
# name = input('请输入您的姓名：')
# age = input('请输入您的年龄：')
# address = input('请输入您的住址：')
#
# print('我的名字是{}，今年{}岁了，家里住在{}...'.format(name, age, address))
#
# # f形式（Python3）
# name = input('请输入您的姓名：')
# age = input('请输入您的年龄：')
# address = input('请输入您的住址：')
#
# print(f'我的名字是{name}，今年{age}岁了，家里住在{address}...')

# 字符串 切片
# 顾头不顾尾：
# 序列名称[开始位置下标:结束位置下标:步长]
# ① 不包含结束位置下标对应的数据， 正负整数均可；
# ② 步长是选取间隔，正负整数均可，正数从左向右，负数从右向左。默认步长为1。
# 起始位置与结束位置都是负数（遵循一个原则：必须是从左向右截取）
num="0123456789"
print(num[-8:-1])
print(num[0:8])

str4="apple"
# find 若是找到 直接返回下标 若是没找到 则返回-1
print(str4.find("l"))
print(str4.rfind("m"))
# index若是找到 直接返回下标 若是没找到 会报错
# print(str4.index("m"))


str1 = 'python'
# 左对齐
print(str1.ljust(10, '.'))
# 右对齐
print(str1.rjust(10, '#'))
# 居中对齐
print(str1.center(10, '@'))


