from sklearn.datasets import load_boston
from sklearn.linear_model import SGDRegressor,LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 获取数据
data = load_boston()
# 数据划分
x_train, x_test, y_train, y_test = train_test_split(data.data, data.target,
                                                    test_size=0.2,
                                                    random_state=22)
# 特征工程-标准化
transfer = StandardScaler()
transfer.fit_transform(x_train)
transfer.fit_transform(x_test)
#采用随机平均梯度回归
estimator = SGDRegressor()
estimator.fit(x_train,y_train)
predict = estimator.predict(x_test)
#直接采取线性回归
lineReg = LinearRegression()
lineReg.fit(x_train,y_train)
line_predict = lineReg.predict(x_test)

print("梯度下降误差为:\n", mean_squared_error(y_test, predict))
print("线性下降误差为:\n", mean_squared_error(y_test, line_predict))