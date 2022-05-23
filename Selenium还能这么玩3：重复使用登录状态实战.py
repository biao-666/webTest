#! python3
'''
从名利行运行python脚本就需要下面这行
在Windows上，第一行是#! python3。
在OS X上，第一行是#! /usr/bin/env/python3。
在Linux上，第一行是#! /usr/bin/python3。
'''

from selenium import webdriver
from time import sleep
import yaml

def login():
    # 定义为全局变量浏览器才不会自动关闭
    global driver11
    driver11 = webdriver.Edge()
    driver11.get('这里填入url')
    driver11.find_element('id', 'merchant_name').send_keys('')
    driver11.find_element('id', 'username').send_keys('')
    driver11.find_element('id', 'password').send_keys('')
    driver11.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[4]/div/div/span/button').click()
    sleep(3)
    remote_executor = driver11.command_executor._url
    session_id = driver11.session_id
    return remote_executor,session_id

# 持久化存储
def save_session(executor, sid):
    service = dict(remote_executor=executor,
                   session_id=sid)
    with open('session.yaml', 'w', encoding='utf-8') as f:
        yaml.safe_dump(service, f)
    return service

remote_executor,session_id = login()
save_session(remote_executor,session_id)

# 获取持久化的session
caps = {
  "capabilities": {
    "firstMatch": [
      {"browserName": "chrome"},
    ]
  }
}
def read_service():
    with open('session.yaml', encoding='utf-8') as f:
        session = yaml.safe_load(f)
    return session

def reuse_session(executor, session_id):
    driver2 = webdriver.Remote(executor,
                               desired_capabilities=caps)
    driver2.close()
    driver2.session_id = session_id
    return driver2

session_config = read_service()
print(session_config)
executor = session_config['remote_executor']
session_id = session_config['session_id']
driver = reuse_session(executor, session_id)

# script1
driver.get('这里填入url')
sleep(5)


