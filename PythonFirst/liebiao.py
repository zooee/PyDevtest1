#encoding:utf-8
'''
Created on 2016年3月25日

@author: Administrator
'''
#列表生成式
L = [x * x for x in range(1, 101) if x % 2 == 0]
print L
L2 = [m + n for m in 'ABC' for n in 'ABC']
print L2

##导入os模块
import os
L3 = [dr for dr in os.listdir('.')]
print L3

List = {'Duo':'1', 'lai':'2', 'mi':'3', 'fa':'4', 'suo':'5'}
for k, v in List.iteritems():    #同时迭代key和value
    print k + '=' + v
#使用列表生成式迭代key和value
ResultList = [k + '=' + v for k, v in List.iteritems()]
print ResultList

upper = ['Hello', 'World', 'IBM', 'Apple']
lower = [s.lower() for s in upper]  #把所有大写字母串变成小写
print lower

upper2 = ['HelloBang', 19, 'World', 'IBM', 'Apple']
lower2 = [s.lower() for s in upper2 if isinstance(s,str)]
#lower2 = [s.lower() if isinstance(s,str) else s for s in upper2 ]
print lower2
