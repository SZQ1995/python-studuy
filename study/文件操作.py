import os

"""
在Python，使用open()函数，可以打开一个已经存在的文件，或者创建一个新文件，语法如下：
f = open(name, mode)
注：返回的结果是一个file文件对象（后续会学习，只需要记住，后续方法都是f.方法()）

name：是要打开的目标文件名的字符串(可以包含文件所在的具体路径)。

mode：设置打开文件的模式(访问模式)：只读r、写入w、追加a等。
> r模式：代表以只读模式打开一个已存在的文件，后续我们对这个文件只能进行读取操作。如果文件不存在，则直接报错。另外，r模式在打开文件时，会将光标放在文件的一行。

> w模式：代表以只写模式打开一个文件，文件不存在，则自动创建该文件。w模式主要是针对文件写入而定义的模式。但是，要特别注意，w模式在写入时，光标也是置于第一行同时还会清空原有文件内容。

> a模式：代表以追加模式打开一个文件，文件不存在，则自动创建该文件。a模式主要也是针对文件写入而定义模式。但是和w模式有所不同，a模式不会清空文件的原有内容，而是在文件的尾部追加内容。


write函数写入文件
基本语法
f.write('要写入的内容，要求是一个字符串类型的数据')

close函数关闭文件
f.close()
"""
# 1、打开文件
f = open('python.txt', 'w')
# 2、写入内容
for i in range(5):
    f.write('人生苦短，我学Python！\n')
# 3、关闭文件
f.close()

# 解决写入中文乱码问题
# f = open('python.txt', 'w', encoding='utf-8')

# 文件的读取操作
f = open("python.txt", "r")
content = f.read()  # 读取文件的所有内容
print(content)
f.read(1024)  # 读取1024个字节长度文件内容，字母或数字，一个占1个字节长度。中文utf-8占3个字节长度

# `readlines()方法`：主要用于文本类型数据的读取
# readlines可以按照行的方式把整个文件中的内容进行一次性读取，并且返回的是一个列表，其中每一行的数据为一个元素。
readlines = f.readlines()
for i in readlines:
    print(i)
f.close()

"""
## seek函数移动光标

无论是文件读操作，还是写操作。其起始位置都是文件光标决定的。

r => 文件头
w => 清空文件内容，指向文件头
a => 文件尾

f.seek(offset,whence=0)

offset：开始的偏移量，也就是代表需要移动偏移的字节数
whence：给offset参数一个定义，表示要从哪个位置开始偏移；
        0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。
"""
f = open('python.txt', 'rb+')
f.write(b'0123456789abcdef')
# 16
f.seek(5)  # 从0开始向右移动5个字节
# 5
f.read(1)
# b'5'
f.seek(-3, 2)  # 从右向左移动3个字节
# 13
f.read(1)
# b'd'
f.close()

"""
os模块
在Python中文件和文件夹的操作要借助os模块里面的相关功能，具体步骤如下：
第一步：导入os模块
import os
第二步：调用os模块中的相关方法
os.函数名()
"""
# 对文件进行重命名操作
os.rename("python.txt", "py.txt")
# 对文件进行删除操作
os.remove("py.txt")

# 与文件夹操作相关操作

# 创建一个指定名称的文件夹
# os.mkdir(新文件夹名称)

# current work   directory，获取当前目录名称
# os.getcwd()

# change  directory，切换目录
# os.chdir(切换后目录名称)

# 获取指定目录下的文件信息，返回列表
# os.listdir(目标目录)

# 用于删除一个指定名称的"空"文件夹
# os.rmdir(目标目录)

# 递归删除非空目录
# 需要导入shutil模块
import shutil
# 递归删除非空目录
shutil.rmtree('要删除文件夹路径')