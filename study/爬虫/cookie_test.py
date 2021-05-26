import requests

"""
带cookie请求 
法一：可以在headers字段中包括来进行设置 
法二：利用关键字参数 cookies= 来进行传值
"""
url='http://www.baidu.com'
# response = requests.get(url,headers={'Cookie':'value'})
# response = requests.get(url,cookies={'key':'value'})



#cookiejar的操作
response = requests.get(url)
print(response.cookies)
dict_cookie=requests.utils.dict_from_cookiejar(response.cookies)
print(dict_cookie)
#可以转换回来 不过会丢失域名
cookie_jar=requests.utils.cookiejar_from_dict(dict_cookie)
print(cookie_jar)