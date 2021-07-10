import random
from pylab import mpl
import matplotlib.pyplot as plt

"""
多个坐标系显示
plt.subplts(面向对象的画图方法)
"""
# 0.准备数据
x = range(60)
y_shanghai = [random.uniform(15, 18) for i in x]
y_beijing = [random.uniform(1, 5) for i in x]
# 1.创建画布
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 8), dpi=100)
# 2.绘制图像
axes[0].plot(x,y_shanghai,color='r',label='上海')
axes[1].plot(x,y_beijing,color='b', linestyle="--",label='北京')
#构造x y轴的刻度标签
x_ticks_label=["11点{}分".format(i) for i in x]
# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]
y_ticks=range(40)
#刻度显示
axes[0].set_xticks(x[::5])
axes[0].set_yticks(y_ticks[::5])
axes[0].set_xticklabels(x_ticks_label[::5])

axes[1].set_xticks(x[::5])
axes[1].set_yticks(y_ticks[::5])
axes[1].set_xticklabels(x_ticks_label[::5])
#添加网格显示
axes[0].grid(True,linestyle='--',alpha=0.5)
axes[1].grid(True,linestyle='--',alpha=0.5)

#添加描述信息
axes[0].set_xlabel('时间')
axes[0].set_ylabel('温度')
axes[0].set_title('中午11点--12点某城市温度变化图',fontsize=20)
axes[1].set_xlabel('时间')
axes[1].set_ylabel('温度')
axes[1].set_title('中午11点--12点某城市温度变化图',fontsize=20)

# 添加图例
axes[0].legend(loc=0)
axes[1].legend(loc=0)

plt.show()

