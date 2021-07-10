from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

#  构造训练集
x_train = np.array([[88, 11],[87, 11],[88, 12],[89, 12],
                    [87, 13],[89, 13],[88, 14],[90, 14],
                    [90, 15]])
y_train = np.array(
    [5.382, 5.299, 5.358, 5.292, 5.602, 6.014, 5.830, 6.102, 6.075])
# 输入测试集
x_test = np.array([[89, 11],
                   [91, 16]])
y_test = np.array([5.547, 6.414])
reg = LinearRegression()  # 创建学习器对象
reg.fit(x_train, y_train)  # 训练模型
predict = reg.predict(x_test)# 对测试集进行预测
print(predict)
print(reg.score(x_test,y_test))

# 中文支持
# mpl.rcParams['font.sans-serif'] = [u'SimHei']
# mpl.rcParams['axes.unicode_minus'] = False
# # 下面进行可视化
# predict = reg.predict(x_train)
# x = np.linspace(5, 7, 100)
# plt.plot(predict, y_train, 'ro', x, x, 'b--')
# plt.xlabel("预测的因变量")
# plt.ylabel("实际的因变量")
# plt.legend(("预测值x,实际值y", "全部吻合的曲线"))
# plt.show()
