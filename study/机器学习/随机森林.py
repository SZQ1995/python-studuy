from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split, GridSearchCV
import pandas as pd

""""
sklearn.ensemble.RandomForestClassifier(n_estimators=10, criterion=’gini’, max_depth=None, bootstrap=True, random_state=None, min_samples_split=2)
    n_estimators：integer，optional（default = 10）森林里的树木数量120,200,300,500,800,1200
    Criterion：string，可选（default =“gini”）分割特征的测量方法
    max_depth：integer或None，可选（默认=无）树的最大深度 5,8,15,25,30
    max_features="auto”,每个决策树的最大特征数量
    If "auto", then max_features=sqrt(n_features).
    If "sqrt", then max_features=sqrt(n_features)(same as "auto").
    If "log2", then max_features=log2(n_features).
    If None, then max_features=n_features.
    bootstrap：boolean，optional（default = True）是否在构建树时使用放回抽样
    min_samples_split:节点划分最少样本数
    min_samples_leaf:叶子节点的最小样本数
超参数：n_estimator, max_depth, min_samples_split,min_samples_leaf
"""
# 获取数据
data = pd.read_csv("./ttnkh_data.csv")
# 数据基本处理
x = data[["Pclass", "Age", "Sex"]]
y = data["Survived"]
x['Age'].fillna(x['Age'].mean(), inplace=True)
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=22)
# 特征工程
transfer = DictVectorizer(sparse=False)
x_train = transfer.fit_transform(x_train.to_dict(orient="records"))
x_test = transfer.fit_transform(x_test.to_dict(orient="records"))
# 机器学习-随机森林
estimator = RandomForestClassifier()
#定义超参数的选择列表
param = {"n_estimators": [120,200,300,500,800,1200], "max_depth": [5, 8, 15, 25, 30]}
#使用GridSearchCV进行网格搜索
# 超参数调优
gc = GridSearchCV(estimator, param_grid=param, cv=2)
gc.fit(x_train, y_train)
print("随机森林预测的准确率为：", gc.score(x_test, y_test))