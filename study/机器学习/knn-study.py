"""
K- 近邻算法的学习

"""
import pandas as pd
import numpy as np
"""
欧式距离计算
"""
# 初始化坐标数据 生成5个三维坐标
# vector1=np.array(np.random.randint(0,30,3))
# vector2=np.array(np.random.randint(0,30,3))
# vector3=np.array(np.random.randint(0,30,3))
# vector4=np.array(np.random.randint(0,30,3))
# vector5=np.array(np.random.randint(0,30,3))
# #计算欧式距离
# dist1=np.sqrt(np.sum(np.square(vector5-vector1)))
# dist2=np.sqrt(np.sum(np.square(vector5-vector2)))
# dist3=np.sqrt(np.sum(np.square(vector5-vector3)))
# dist4=np.sqrt(np.sum(np.square(vector5-vector4)))
# data=[vector1,vector2,vector3,vector4,vector5]
# #构造列索引
# columns=['x','y','z']
# #构造行索引
# indexs=['坐标' + str(i) for i in range(1,6)]
# #添加距离列
# table = pd.DataFrame(data=data, columns=columns, index=indexs)
# table['distance']=(dist1,dist2,dist3,dist4,0)
# print(table)




