import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
"""
class sklearn.tree.DecisionTreeClassifier(criterion=’gini’, max_depth=None,random_state=None)
    criterion
        特征选择标准
        "gini"或者"entropy"，前者代表基尼系数，后者代表信息增益。一默认"gini"，即CART算法。
    min_samples_split
        内部节点再划分所需最小样本数
        这个值限制了子树继续划分的条件，如果某节点的样本数少于min_samples_split，则不会继续再尝试选择最优特征来进行划分。 默认是2.如果样本量不大，不需要管这个值。如果样本量数量级非常大，则推荐增大这个值。我之前的一个项目例子，有大概10万样本，建立决策树时，我选择了min_samples_split=10。可以作为参考。
    min_samples_leaf
        叶子节点最少样本数
        这个值限制了叶子节点最少的样本数，如果某叶子节点数目小于样本数，则会和兄弟节点一起被剪枝。 默认是1,可以输入最少的样本数的整数，或者最少样本数占样本总数的百分比。如果样本量不大，不需要管这个值。如果样本量数量级非常大，则推荐增大这个值。之前的10万样本项目使用min_samples_leaf的值为5，仅供参考。
    max_depth
        决策树最大深度
        决策树的最大深度，默认可以不输入，如果不输入的话，决策树在建立子树的时候不会限制子树的深度。一般来说，数据少或者特征少的时候可以不管这个值。如果模型样本量多，特征也多的情况下，推荐限制这个最大深度，具体的取值取决于数据的分布。常用的可以取值10-100之间
    random_state
        随机数种子
"""
# 获取泰坦尼克号乘客生存预测数据
data = pd.read_csv("./ttnkh_data.csv")
#确定特征值,目标值
x=data[["Pclass","Age","Sex"]]
y = data["Survived"]
#缺失值处理，年龄属性有部分缺失 用平均值代替
x['Age'].fillna(x['Age'].mean(), inplace=True)
#训练集 测试集划分
x_train,x_test,y_train,y_test = train_test_split(x, y, random_state=22)
#特征工程-字典特征提取
transfer = DictVectorizer(sparse=False)
x_train = transfer.fit_transform(x_train.to_dict(orient="records"))
x_test = transfer.fit_transform(x_test.to_dict(orient="records"))
# 机器学习(决策树)
estimator = DecisionTreeClassifier(criterion="entropy", max_depth=5)
estimator.fit(x_train, y_train)
# 模型评估
print(estimator.score(x_test, y_test))
print(estimator.predict(x_test))