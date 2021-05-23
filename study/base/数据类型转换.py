num=input("请输入您的幸运数字")
print(type(num))
print("_"*20)
num=int(num)
print(type(num))

# eval 方法 将字符串中数字转换为原数据类型
price=input("请输入商品价格：")
print(eval(price))
print(type(eval(price)))
# str="10" 经过eval(str) 转换成int类型
# str="10.88" 经过eval(str) 转换成float类型



print(type(float(num)))
print(type(str(num)))
# 注意 int类型转成float类型时候，小数点后面的数据会丢失