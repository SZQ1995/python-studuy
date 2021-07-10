"""
plot绘制数学图像

利用Numpy
numpy介绍【了解】
一个开源的Python科学计算库
计算起来要比python简洁高效
Numpy使用ndarray对象来处理多维数组
ndarray介绍【了解】
NumPy提供了一个N维数组类型ndarray，它描述了相同类型的“items”的集合。
生成numpy对象:np.array()
ndarray的优势【掌握】
内存块风格
list -- 分离式存储,存储内容多样化
ndarray -- 一体式存储,存储类型必须一样
ndarray支持并行化运算（向量化运算）
ndarray底层是用C语言写的,效率更高,释放了GIL
Numpy专门针对ndarray的操作和运算进行了设计，所以数组的存储效率和输入输出性能远优于Python中的嵌套列表，数组越大，Numpy的优势就越明显。
"""

import  numpy as np
import matplotlib.pyplot as plt

#代表从-10 到10 直接申请1000个数据
x= np.linspace(-10,10,1000)
#sin函数
y=np.sin(x)

#创建画布
plt.figure(figsize=(20,8),dpi=100)
#绘制
plt.plot(x,y)
plt.grid()
plt.show()

