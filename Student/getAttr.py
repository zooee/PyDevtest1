#coding=utf-8
'''
Created on 2016年4月5日

@author: Administrator
'''
class Student(object):
    def __init__(self):
        self.name = 'Michael'
    def __getattr__(self, attr):
        if attr == 'score':
            return 98
s = Student()
print s.name
print s.age