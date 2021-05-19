"""
基本语法：

try:
    可能遇到异常的代码
except 异常类型:
    捕获到对应的错误以后，执行的代码

"""

# 案例：捕获FileNotFoundError异常

try:
    f = open('pp.txt', 'r')
except FileNotFoundError as  e:
    print(e)

# 同时捕获多个异常
try:
    print(name)
    # print(10/0)
except (NameError, ZeroDivisionError) as e:
    print(e)

# 捕获所有未知异常
try:
    pass
except Exception as e:
    print(e)

# 异常捕获中else语句
try:
    pass
except Exception as e:
    print(e)
else:
    print("真开心，我没有遇到任何异常")

# 异常捕获中的finally语句
# finally表示的是无论是否异常都要执行的代码，例如关闭文件、关闭数据库连接。
try:
    f = open('python.txt', 'r')
except:
    f = open('python.txt', 'w')
else:
    print('哈哈，真开森，没有遇到任何异常')
finally:
    print('关闭文件')
    f.close()


# raise 抛出异常
# 在Python中，抛出自定义异常的语法为`raise 异常类对象`
def input_password():
    password = input('请输入您的密码，不少于6位：')
    if len(password) < 6:
        # 抛出异常
        raise Exception('您的密码长度少于6位')
        return
    # 如果密码长度正常，则直接显示密码
    print(password)


input_password()


# 自定义异常类---继承Exception
class ShortException(Exception):
    def __init__(self, len):
        self.len = len

    def __str__(self):
        return f"您输入的密码长度为{self.name},不符合输入要求"


try:
    password = input('请输入您的密码，不少于6位：')
    if len(password) < 6:
        # 抛出异常
        raise ShortException(len(password))
#这里直接捕获异常
except Exception as  e:
    print(e)
else:
    # 如果密码长度正常，则直接显示密码
    print(password)
