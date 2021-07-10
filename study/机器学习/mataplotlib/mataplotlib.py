import matplotlib.pyplot  as plt
from pylab import mpl
import random

"""
为什么要学习Matplotlib
可视化是在整个数据挖掘的关键辅助工具，可以清晰的理解数据，从而调整我们的分析方法。
能将数据进行可视化,更直观的呈现
使数据更加客观、更具说服力

定义
    主要用于开发2D图标（3D）
    数据分析，基于分析，进行展示
绘图流程
    创建画布
    绘制图像
    显示图像
matplotlib三层次结构
    容器层
        canvas
        figure
        axes
    辅助显示层
        添加x轴，y轴描述，标题....
    图像层
        绘制什么图像的声明
"""

"""
1.创建画布 -- plt.figure()
    plt.figure(figsize=(), dpi=)
        figsize:指定图的长宽
        dpi:图像的清晰度
        返回fig对象
2.绘制图像 -- plt.plot(x, y)
3.显示图像 -- plt.show()
"""
plt.figure(figsize=(10, 10), dpi=100)
plt.plot([1, 2, 3, 4, 5, 6, 7], [17, 17, 18, 15, 11, 11, 13])
# 进行保存 一定要放在show前面
# plt.savefig(r"C:\Users\SZQ\Desktop\aaa.png")
# plt.show()会释放figure资源，如果在显示图像之后保存图片将只能保存空图片。
plt.show()

"""
折线图
下面以温度图为例
"""
# 准备x y轴数据
x = range(60)
y_shanghai = [random.uniform(10, 15) for i in x]
# 创建画布
plt.figure(figsize=(10, 10), dpi=100)
# 绘制折线图
plt.plot(x, y_shanghai)
# 添加自定义 x y的刻度
x_ticks_label = ["11点{}分".format(i) for i in x]
y_ticks = range(40)
# 修改x y轴 坐标的刻度显示
plt.xticks(x[::5], x_ticks_label[::5])
plt.yticks(y_ticks[::5])
# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]
# 设置正常显示符号
mpl.rcParams["axes.unicode_minus"] = False
# 添加网格显示  ----为了更加清楚地观察图形对应的值
plt.grid(True, linestyle='--', alpha=0.5)
# 2.3 添加描述信息
plt.xlabel("时间")
plt.ylabel("温度")
plt.title("中午11点--12点某城市温度变化图", fontsize=20)
# plt.show()

"""
一个坐标系中绘制多个图像
即---多次plot
在上一个温度图的基础上 添加一个新的城市
"""

# 增加北京的温度数据
y_beijing = [random.uniform(8, 10) for i in x]
# 绘制折线图
# plt.plot(x, y_beijing)
# 使用多次plot 可以画多个折线
# r 红色	- 实线
# g 绿色	- - 虚线
# b 蓝色	-. 点划线
# w 白色	: 点虚线
# c 青色	' ' 留空、空格
# m 洋红
# y 黄色
# k 黑色
plt.plot(x, y_beijing, color='r', linestyle='--',label="北京")
# plt.show()

"""
注意：如果只在plt.plot()中设置label还不能最终显示出图例，还需要通过plt.legend()将图例显示出来。

"""
# 显示图例 best即0
plt.legend(loc="best")
plt.show()


#柱状图
plt.bar(x,height=11)


