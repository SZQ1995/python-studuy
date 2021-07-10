import time

from selenium import webdriver


driver = webdriver.Chrome(executable_path='../chromedriver')
driver.get("http://www.itcast.cn/")
driver.set_window_position(1000,500)
time.sleep(10000)
driver.quit()
