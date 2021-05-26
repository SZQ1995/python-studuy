"""
通过pytesseract模块的 image_to_string
方法就能将打开的图片文件中的数据提取成字符串数据，具体方法如下

"""

from PIL import  Image
import  pytesseract

im=Image.open('./image_test.jpg')
result=pytesseract.image_to_string(im)
print(result)