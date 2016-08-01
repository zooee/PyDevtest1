#encoding:utf-8
'''
Created on 2016年3月4日

@author: Administrator
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
first_url = "http://ids.youkeyijia.com/"
browser.get(first_url)
time.sleep(3)

browser.find_element_by_id("username").clear()
#Keys.tab清除输入框内容
browser.find_element_by_id("username").send_keys(Keys.TAB)
browser.find_element_by_id("username").send_keys("qqqq")
#全选
browser.find_element_by_id("username").send_keys(Keys.CONTROL,'a')
time.sleep(3)
#剪切
browser.find_element_by_id("username").send_keys(Keys.CONTROL,'x')
#重新输入内容
browser.find_element_by_id("username").send_keys("qubu")
time.sleep(3)
browser.find_element_by_id("password").send_keys(Keys.TAB)   
browser.find_element_by_id("password").send_keys("uoko123")
#Keys.ENTER代替键盘Enter
browser.find_element_by_class_name("main-form-button").send_keys(Keys.ENTER)
time.sleep(3)


browser.quit()

    
