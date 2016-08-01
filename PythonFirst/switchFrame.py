#coding=utf-8
'''
Created on 2016年5月18日

@author: Administrator
'''
from selenium import webdriver
import time
import os

browser = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('HTML/frame.html')

browser.get(file_path)
time.sleep(3)
browser.switch_to_frame('f1')
browser.switch_to_frame('f2')
browser.find_element_by_id('kw').send_keys('python')
browser.find_element_by_id('su').click()
time.sleep(3)
browser.quit()

