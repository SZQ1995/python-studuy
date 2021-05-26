import time

from selenium import webdriver


driver = webdriver.Chrome(executable_path='../chromedriver')
driver2 = webdriver.Chrome(executable_path='../chromedriver')
driver3 = webdriver.Chrome(executable_path='../chromedriver')
driver.get("http://www.itcast.cn/")
driver2.get("http://www.itcast.cn/")
driver3.get("http://www.itcast.cn/")
time.sleep(10000)
driver.quit()
