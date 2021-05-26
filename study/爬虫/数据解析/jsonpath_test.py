import json

import jsonpath

data = {'key1': {'key2': {'key3': {'key4': {'key5': {'key6': 'python'}}}}}}

print(data['key1']['key2']['key3']['key4']['key5']['key6'])

"""
jsonpath 语法(常用3个)
$ 表示根节点--最外层的大括号
. 子节点
.. 内部任意位置，子孙节点
"""
# 利用jsonpath来进行提取 jsonpath结果为列表 获取数据需要索引
print(jsonpath.jsonpath(data, '$.key1.key2.key3.key4.key5.key6')[0])
print(jsonpath.jsonpath(data, '$..key6')[0])

data = '{"employees":[{"firstName":"Bill","lastName":"Gates"},{ "firstName":"George" ,"lastName":"Bush"},{"firstName": "Thomas", "lastName": "Carter"}]}'
#先将json字符串 转换为 字典对象 才能进行jsonpath解析
data_dict=json.loads(data)
#打印出所有firstName
print(jsonpath.jsonpath(data_dict,"$..lastName"))