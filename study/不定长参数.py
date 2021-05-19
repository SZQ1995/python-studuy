"""
包裹(packing)位置参数
不定长参数 是以*打头
组成的是 元组类型
"""


def user_info(*args):
    print(args)
    # 也可以等价于
    print(f'我的名字{args[0]}，今年{args[1]}岁了，住在{args[2]}')


# 调用函数，传递参数
user_info('Tom', 23, '美国纽约')  # ('Tom', 23, '美国纽约')

"""
包裹关键字参数
组成的是 字典类型
"""


def user_info(**kwargs):
    print(kwargs)  # 字典类型数据，对传递参数没有顺序要求，格式要求key = value值
    print(f'我的名字{kwargs["name"]}，今年{kwargs["age"]}岁了，住在{kwargs["address"]}')


# 调用函数，传递参数
user_info(name='Tom', address='美国纽约', age=23)
