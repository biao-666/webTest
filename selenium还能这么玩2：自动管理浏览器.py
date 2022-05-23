#! python3
'''
从名利行运行python脚本就需要下面这行
在Windows上，第一行是#! python3。
在OS X上，第一行是#! /usr/bin/env/python3。
在Linux上，第一行是#! /usr/bin/python3。
'''

from selenium import webdriver

# 半永久的 chrome session
driver = webdriver.Edge()
driver.get('http://www.baidu.com')

# 获取 service url 和 session_id
remote_executor = driver.command_executor._url
session_id = driver.session_id
print(remote_executor, session_id)

# 连接之前的 session
caps = {
  "capabilities": {
    "firstMatch": [
      {"browserName": "chrome"},
    ]
  }
}
driver2 = webdriver.Remote(remote_executor, desired_capabilities=caps)
driver2.close()
driver2.session_id = session_id

driver2.find_element('id', 'kw').send_keys('hello')