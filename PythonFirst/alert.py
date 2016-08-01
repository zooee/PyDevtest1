#coding=utf-8
'''
Created on 2016年6月3日

@author: Administrator
'''
from selenium import webdriver
import os,time

driver = webdriver.Firefox()
file_path = 'File:///' + os.path.abspath('HTML/alert.html')

driver.get(file_path)
time.sleep(3)

browser = driver.find_element_by_id("ShippingMethod")
time.sleep(3)
browser = driver.find_element_by_xpath(".//option[@value='10.69']").click()
time.sleep(3)
driver.quit()