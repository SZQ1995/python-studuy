import requests

#有网站提示 非私密链接 不安全提示 可以设置verify=False 来忽略
requests.get('xxxxx',verify=False)