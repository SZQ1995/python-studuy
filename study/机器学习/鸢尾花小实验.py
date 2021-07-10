# 导入模块
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

# 获取鸢尾花的数据集
iris = load_iris()
# 数据基本处理
# x_train,x_test,y_train,y_test为训练集特征值、测试集特征值、训练集目标值、测试集目标值
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target,
                                                    test_size=0.2,
                                                    random_state=22)
# 特征工程 -比如进行归一化，标准化
# 这里进行标准化
transfer = StandardScaler()
x_train = transfer.fit_transform(x_train)
x_test = transfer.transform(x_test)
# 实例化预估器类 -机器学习（模型预测）-使用knn算法 使用kd树
estimator=KNeighborsClassifier(n_neighbors=6,algorithm="kd_tree")
estimator.fit(x_train, y_train)

# 模型评估
# 方法一 比对真实值和预测值
y_predict = estimator.predict(x_test)
print("预测结果为:", y_predict)
print("比对真实值和预测值：", y_predict == y_test)
# 方法二 直接计算准确率
score = estimator.score(x_test, y_test)
print("准确率：", score)
