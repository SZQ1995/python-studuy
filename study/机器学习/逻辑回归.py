import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression,LogisticRegressionCV

# 获取数据
names = ['Sample code number', 'Clump Thickness', 'Uniformity of Cell Size',
         'Uniformity of Cell Shape',
         'Marginal Adhesion', 'Single Epithelial Cell Size', 'Bare Nuclei',
         'Bland Chromatin',
         'Normal Nucleoli', 'Mitoses', 'Class']
data = pd.read_csv(
    "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data",
    names=names)
# 缺失值处理
data = data.replace(to_replace="?", value=np.NaN)
data = data.dropna()
# 数据划分 对表格进行切片提取0-9列数据作为特征值
x = data.iloc[:, 1:10]
y = data["Class"]
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=22)
# 特征工程-数据标准化
transform = StandardScaler()
x_train = transform.fit_transform(x_train)
x_test = transform.fit_transform(x_test)
# 机器学习-逻辑回归 solver是指优化算法可以默认 我这里选择sag
logistic_regression = LogisticRegression(solver="sag")
logistic_regression.fit(x_train, y_train)
predict = logistic_regression.predict(x_test)
print(predict)
# 模型评估
print(logistic_regression.score(x_test, y_test))
