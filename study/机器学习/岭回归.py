from sklearn.datasets import load_boston
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = load_boston()
x_train, x_test, y_train, y_test = train_test_split(data.data, data.target,
                                                    random_state=22)
transfer = StandardScaler()
x_train = transfer.fit_transform(x_train)
x_test = transfer.fit_transform(x_test)
# 岭回归 如果添加normalize=True 就不需要上面的手动标准化  Ride会自动进行标准化
estimator = Ridge(alpha=1.2)
estimator.fit(x_train, y_train)
predict = estimator.predict(x_test)
print("预测值为", predict)
