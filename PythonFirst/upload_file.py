#encoding:utf-8
'''
Created on 2016��3��7��

@author: Administrator
'''
from selenium import webdriver
import os, time

driver = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('HTML/Upload_file.html')
driver.get(file_path)

driver.find_element_by_name("file").send_keys('E:\Mine\abc.txt')

time.sleep(3)