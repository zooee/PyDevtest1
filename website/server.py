#coding=utf-8
'''
Created on 2016年5月12日

@author: Administrator
'''
from wsgiref.simple_server import make_server
from homePage import application

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 8000, application)
print ('serving Http on port 8000...')

httpd.serve_forever()

print 'hello'
print 'hello'
print 'hello'

