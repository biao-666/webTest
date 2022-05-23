#! python3
'''
从名利行运行python脚本就需要下面这行
在Windows上，第一行是#! python3。
在OS X上，第一行是#! /usr/bin/env/python3。
在Linux上，第一行是#! /usr/bin/python3。
'''

from selenium import webdriver
from time import sleep

# 创建浏览器驱动对象
driver = webdriver.Edge() # Edge浏览器

# 打开指定网址
driver.get('https:www.baidu.com')
# 休眠
sleep(3)
# 关闭浏览器驱动对象
driver.quit()