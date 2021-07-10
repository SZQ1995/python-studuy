# 导入模块
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

# 获取鸢尾花的数据集
iris = load_iris()
# 数据基本处理
# x_train,x_test,y_train,y_test为训练集特征值、测试集特征值、训练集目标值、测试集目标值
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2,random_state=22)
# 特征工程 -比如进行归一化，标准化
# 这里进行标准化
transfer = StandardScaler()
x_train = transfer.fit_transform(x_train)
x_test = transfer.transform(x_test)
# 实例化预估器类
estimator = KNeighborsClassifier()
# 模型选择与调优——网格搜索和交叉验证，cv=3表示3则交叉验证
param_dict = {"n_neighbors": [1, 3, 5, 7, 9]}
estimator = GridSearchCV(estimator, param_grid=param_dict, cv=10, n_jobs=-1)
# fit数据进行训练
estimator.fit(x_train, y_train)
# 评估模型效果
# 方法a：比对预测结果和真实值
y_predict = estimator.predict(x_test)
print("比对预测结果和真实值：\n", y_predict == y_test)
# 方法b：直接计算准确率
score = estimator.score(x_test, y_test)
print("直接计算准确率：\n", score)

print("最好结果：\n", estimator.best_score_)
print("最好的参数模型：\n", estimator.best_estimator_.__dict__)
print("整体模型结果：\n", estimator.cv_results_)
