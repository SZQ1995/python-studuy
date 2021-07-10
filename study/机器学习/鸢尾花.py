from sklearn.datasets import load_iris,fetch_20newsgroups
import seaborn as sns
import matplotlib.pyplot as plt
import  pandas as  pd

#数据集的获取
#1.1小数据集的获取
iris=load_iris()
# print(iris)

#1.2大数据集获取
news=fetch_20newsgroups();
# print(news)

#2.数据集属性描述
# print("数据集中特征值是:\n",iris.data)
# print("数据集中目标值是:\n",iris["target"])
# print("数据集中特征值名字是:\n",iris.feature_names)
# print("数据集中目标值名字是:\n",iris.target_names)
# print("数据集的描述是:\n",iris.DESCR)


#把数据化成dataframe的格式
iris_d=pd.DataFrame(data=iris['data'],columns=['Sepal_length','Sepal_width','Petal_length','Petal_width'])
#给表格添加一列
iris_d['Species']=iris.target
# print(iris_d)

def plot_iris(data,col1,clo2):
    #x y表示具体x轴 y轴的的索引值 data是具体数据 hue是目标值 fit_reg 是否进行线性拟合
    sns.lmplot(x=col1,y=clo2,data=data,hue="Species",fit_reg=False)

    plt.title("鸢尾花数据展示")
    plt.xlabel(col1)
    plt.ylabel(clo2)
    plt.show()

plot_iris(iris_d,'Sepal_length','Petal_width')