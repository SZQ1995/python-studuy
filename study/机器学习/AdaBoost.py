from sklearn.ensemble import AdaBoostClassifier
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
import pandas as pd
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
# 机器学习-AdaBoost
# n_estimators表示要组合的弱分类器个数；
# algorithm可选{‘SAMME’, ‘SAMME.R’}，默认为‘SAMME.R’，表示使用的是real boosting算法，‘SAMME’表示使用的是discrete boosting算法
estimator = AdaBoostClassifier(n_estimators=100,algorithm="SAMME.R")
estimator.fit(x_train,y_train)
print("AdaBoost预测的准确率为：", estimator.score(x_test, y_test))