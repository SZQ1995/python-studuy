"""

requests模块中的Session类能够自动处理发送请求获取响应过程中
产生的cookie，进而达到状态保持的目的
session的作用：
自动处理cookie 即 下一次请求会带上前一次的cookie
session应用场景：
自动处理连续的多次请求过程中产生的cookie
"""
import requests

# 实例化session对象
session = requests.session()
# 直接用session进行请求即可
response = session.get('http://www.baidu.com', headers='')
response = session.post('http://www.baidu.com', headers='')
#也可以这么给session添加headers
session.headers={}