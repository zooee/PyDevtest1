
'''
Created on 2016年4月15日

@author: Administrator
'''
import os
#str:查找的字符串
#path:路径，默认为当前路径
#the_path:相对路径
def what_file(str,path=".",the_path = "\\" ):
    for p in os.listdir(path):
        #当前文件全路径
        current_file = os.path.join(path,p)
        #是否存在str字符串
        if str in p and os.path.isfile(current_file):
            print(p,os.path.join(the_path,p))#输出相对路径
        #当前路径是否一个文件夹
        if os.path.isdir(current_file):
            #是文件夹递归，并将相对路径加上p
            what_file(str,current_file,os.path.join(the_path,p))
#调用
what_file("py")
'''
import json
d = dict(name = 'zoe', age = 18, score = 99)
json.dumps(d)
#t = open('json.txt', 'wb')
#json.dump(d, t)
'{"name": "zoe", "age": 18, "score": 99}'
json_str = '{"name": "zoe", "age": 18, "score": 99}'
json.loads(json_str)
{'name': 'zoe', 'age': 18, 'score': 99}
'''