#coding=utf-8
'''
Created on 2016年6月14日

@author: Administrator
'''
from selenium import webdriver
import time

driver = webdriver.Firefox()
url = "http://mail.163.com" 
driver.get(url)

print ('------------------Before login---------------------------')

#打印当前title
title = driver.title
print (title)
#打印当前url
now_url = driver.current_url
print(now_url)

#执行邮箱登录
driver.find_element_by_id("idInput").clear()
driver.find_element_by_id("idInput").send_keys("18782965509")
driver.find_element_by_id("pwdInput").clear()
driver.find_element_by_id("pwdInput").send_keys("1018zooee.")
driver.find_element_by_id("loginBtn").click()

print ('------------------After login-------------------------')
#打印当前title
title = driver.title
print (title)
#打印当前url
now_url = driver.current_url
print(now_url)

#获得登陆的用户名
try:
    user = driver.find_element_by_id("spnUid").text
except Exception as msg:
    print (msg)
time.sleep(4)
#driver.quit()
