# encoding:utf-8
'''
Created on 2016年3月7日

@author: Administrator
'''
from selenium import webdriver
import time , os

browser = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('HTML/frame.html')
browser.get(file_path)

browser.implicitly_wait(30)
browser.switch_to_frame("f1")
browser.switch_to_frame("f2")

browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()

time.sleep(3)
browser.quit()
