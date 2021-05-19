
n=5
while n>0:
    m=0
    while m<5:
        print("*",end=" ")
        m+=1;
    print("")
    n-=1;

"""
for循环功能非常强大，可以自动判断序列的长度，
长度为多少，则for循环就循环多少次。
每次循环时，系统会自动将序列中的每个元素赋值给变量i，
赋值完成后，for循环内部会自动更新计数器，向后移动一位，
继续循环，直至元素全部循环结束。
"""

str="SZQ1995"
for i in str:
    print(i,end="")


"""
基本语法：
range(stop)
range(start, stop[, step])

start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
stop: 计数到 stop 结束，但不包括 stop。例如：range（0，5） 是 [0, 1, 2, 3, 4] 没有 5
step：步长，默认为1。例如：range（0，5） 等价于 range(0, 5, 1)

range有一个口诀：顾头不顾尾，包含头部信息，但是不包含尾部信息，
如range(10)，则返回0~9之间的序列，又比如range(0, 5)代表返回0 ~ 4之间的序列。
"""
print("")
for i in  range(6):
    print(i,end="")