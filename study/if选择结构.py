if False:
    print('条件成立执行的代码1')
    print('条件成立执行的代码2')

# 下方的代码没有缩进到if语句块，所以和if条件无关
print('我是无论条件是否成立都要执行的代码')

num=int(input("请输入数字"))
if num>8:
    print("大于8")
elif num==8:
    print("等于8")
else:
    print("小于8")