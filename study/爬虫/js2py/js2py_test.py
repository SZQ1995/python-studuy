import js2py

# 创建js执行环境
import requests

context = js2py.EvaJs()

# 加载js文件
big_js = requests.get('xxxxx')
context.execute(big_js);
#执行
context.execute('这类可以执行 上面加载的js文件中里面的方法');
