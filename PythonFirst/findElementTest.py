#encoding:utf-8
'''
Created on 2016年3月4号

@author: Administrator
'''
from selenium import webdriver
import os,time

dr = webdriver.Firefox();
#拼凑一个文件路径
file_path = 'file:///' + os.path.abspath('HTML/test.html')
#浏览器对象打开HTML文件
dr.get(file_path)

#inputs = dr.find_elements_by_tag_name('input')
#for input in inputs:
#    if input.get_attribute('type') == 'checkbox':
#        input.click()
        
checkboxes = dr.find_elements_by_css_selector('input[type=checkbox]')
for checkbox in checkboxes:
    checkbox.click()
time.sleep(3)
#pop()定位列表到最后一个
checkboxes = dr.find_elements_by_css_selector('input[type=checkbox]').pop().click()
time.sleep(3)
#打印当前页面的checkbox数量
print len(dr.find_elements_by_css_selector('input[type=checkbox]'))

#dr.quit()