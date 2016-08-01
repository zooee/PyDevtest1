#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

browser = webdriver.Firefox()

first_url = "http://redmine.uoko.com/"
print ("now access %s" %(first_url))
browser.get(first_url)
browser.implicitly_wait(30)

browser.maximize_window()

browser.find_element_by_id("username").clear()
browser.find_element_by_id("username").send_keys(Keys.CONTROL, 'a')
time.sleep(3)
browser.find_element_by_id("username").send_keys(Keys.CONTROL, 'c')
time.sleep(3)
browser.find_element_by_id("username").send_keys(Keys.CONTROL, 'v')
time.sleep(3)
browser.find_element_by_id("password").clear()
print ("Have cleared the password")
browser.find_element_by_id("password").send_keys("123456")
browser.find_element_by_name("login").send_keys(Keys.ENTER)

'''
second_url = "http://map.baidu.com/"
print ("now access %s" %(second_url))
browser.get(second_url)
time.sleep(3)

print ("back to %s" %(first_url))
browser.back()
time.sleep(3)

print ("forword to %s" %(second_url))
browser.forward()
'''
#browser.find_element_by_id("kw").send_keys("selenium")
#time.sleep(2)
#browser.find_element_by_id("su").click()
#browser.find_element_by_id("su").submit()
#print browser.title
#browser.quit()