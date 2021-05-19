#   / 表示除  可以有小数
#   // 表示整除    9//2=4
#   ** 表示幂指数   2**4 等价于 2*2*2*2


# 四则运算
num1 = 10
num2 = 3

print(f"加+{num1 + num2}")
print(f"除{num1 / num2}")

# 逻辑运算符
# and or not（与 或 非）
flag = True;
print(not flag)
# 注意 python会把0 空字符串和None看成False
# ，其他数值和非空字符串看成True
# 在计算 a and b时，如果a是false，则根据与运算法则，整个结果必为false
# 因此范围a；如果a是true 则整个结果必定取决于b，因此返回b
print(3 and 4)  #结果为 4
print(0 and 4)  #结果为 0


# 三目运算符
# 语句段1 if 条件判断 else 语句段2
max=num1 if num1>num2 else num2
print(max)
