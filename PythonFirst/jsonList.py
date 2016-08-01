#coding=utf-8
'''
Created on 2016年4月20日

@author: Administrator
'''
import json

class Student(object):
    
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
        
    def student2dict(self, std):
        return {
            'name': std.name,
            'age': std.age,
            'score': std.score
        }
s = Student('zzoe', 20, 88)
'''print(json.dumps(s, default=student2dict)

#j = json.dumps(s)
#print (j)
'''