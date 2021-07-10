


"""
 sklearn 使用
"""

from sklearn.neighbors import KNeighborsClassifier

#构造数据集
x = [[0], [1], [2], [3]]
y = [0, 0, 1, 1]
#模型训练 实例化一个估计器 n_neighbors表示参考几个邻居
estimator=KNeighborsClassifier(n_neighbors=2)
#使用fit方法进行训练
estimator.fit(x,y)
print(estimator.predict([[10]]))

