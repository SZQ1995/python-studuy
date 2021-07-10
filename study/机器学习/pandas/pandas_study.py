"""
pandas的优势
增强图表可读性
便捷的数据处理能力
读取文件方便
封装了Matplotlib、Numpy的画图和计算


Pandas中一共有三种数据结构，分别为：Series、DataFrame和MultiIndex（老版本中叫Panel ）。

其中Series是一维数据结构，DataFrame是二维的表格型数据结构，MultiIndex是三维的数据结构。
"""
import pandas as pd
import numpy as np

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 120)

# Series的创建
"""
pd.Series(data=None, index=None, dtype=None)
参数：
data：传入的数据，可以是ndarray、list等
index：索引，必须是唯一的，且与数据的长度相等。如果没有传入索引参数，则默认会自动创建一个从0-N的整数索引。
dtype：数据的类型
"""
# 指定内容，默认索引
print(pd.Series(np.arange(10)))
# 指定索引
print(pd.Series([6.7, 5.6, 3, 10, 2], index=[1, 2, 3, 4, 5]))
# 通过字典数据创建
dict_pd = pd.Series({'red': 100, 'blue': 300})
print(dict_pd)
# Series中提供了两个属性index和values
print(dict_pd.index)
print(dict_pd.values)

# DataFrame的创建
"""
DataFrame是一个类似于二维数组或表格(如excel)的对象，既有行索引，又有列索引
行索引，表明不同行，横向索引，叫index，0轴，axis=0
列索引，表名不同列，纵向索引，叫columns，1轴，axis=1
pd.DataFrame(data=None, index=None, columns=None)
参数：
index：行标签。如果没有传入索引参数，则默认会自动创建一个从0-N的整数索引。
columns：列标签。如果没有传入索引参数，则默认会自动创建一个从0-N的整数索引。
"""
# 生成10名同学，5门功课的数据
score = np.random.randint(40, 100, (10, 5))
# 构造行索引序列
subjects = ["语文", "数学", "英语", "政治", "体育"]
score_df = pd.DataFrame(score, columns=subjects)
# 构造列索引序列
stu = ['同学' + str(i) for i in range(score_df.shape[0])]
score_df = pd.DataFrame(score, columns=subjects, index=stu)
pd.set_option('display.unicode.ambiguous_as_wide', False)#设置列名对齐
pd.set_option('display.unicode.east_asian_width', False)#设置列名对齐
print(score_df)
# DataFrame的属性
# score_df.shape
# 结果 表示有10行5列
# (10, 5)
score_df.head(3)  # 表示前3行，不写则默认前5行
score_df.tail(3)  # 表示后3行，不写则默认后5行
