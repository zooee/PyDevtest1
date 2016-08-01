#coding=utf-8
'''
Created on 2016年4月20日

@author: Administrator
'''

'''
#linux 系统提供fork方法
import os
print('Process (%s) start...' % os.getpid())
pid = os.fork()
if pid == 0:
    print('It is child process and my parent process is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
'''
#Windows提供multiprocessing模块
#from multiprocessing import Process
#import os

import re
print(re.match(r'^\d{3}\-\d{3,8}$', '010-558555'))
print(re.match(r'^\d{3}\-\d{3,8}$', '010  558555'))

strTest = 'a123@sina.com'

if re.match(r'^\w{1,9}\@\w{3,6}\.[A-Za-z]$', strTest):
    print('I am fine')
else:
    print('I am boring')
