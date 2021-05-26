import json

import requests

url='http://www.baidu.com';
response = requests.get(url)

# print(response.content.decode()) #decode()默认是utf-8

#带header请求
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
response_with_headers = requests.get(url,headers=headers)
# print(response_with_headers.content.decode())

#带参数
param={'wd':'福州'}
response_with_params=requests.get(url+"/s",headers=headers,params=param)
print(response_with_params.url)
print(response_with_params.content.decode())

#另外一种接码方式
response_text=requests.get(url+"/s",headers=headers,params=param)
response_text.encoding='utf8'
print(response_text.text)

#设置超时 默认是秒
requests.get(url,timeout=3)

#处理json 将json字符串 转换成字典
loads_dict = json.loads("{'mm':'hhhhh'}")
