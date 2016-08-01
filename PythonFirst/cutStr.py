#encoding:utf-8
'''
Created on 2016年3月24日

@author: Administrator
'''
List = ['Duo', 'lai', 'mi', 'suo', 'la']
#print List[0]
#L = []
#for i in range(3):
#    L.append(List[i])
#print L 
print List[:3]  
print List[0:3]
print List[1:3]
print List[-1:]
print List[-2:]
print List[-2:-1]
T = (0,1,2,3,4,5,6,7,8,9)
List1 = range(100)
Str = 'wanna be'
#print List1
print List1[:10]                #取前十个数据
print List1[-10:]               #取后时隔数据
print List1[10:20]              #取前十到二十个数据
print List1[::2]                #所有数每隔两个取
print List1[30::3]              #从第三十个数开始每隔3个取
print T[:3]   #取Turple的前三个出来，仍然是turple
print Str[6:7]

from collections import Iterable
print isinstance('abcd', Iterable) #判断对象是否可迭代

Dic = {'a':1, 'b':2, 'c':3}
for key in Dic:   #迭代Key
    print key
for value in Dic.itervalues(): #迭代value
    print value
for k, v in Dic.iteritems():  #迭代key：value
    print k, v
for i, value in enumerate(List): #对list实现类似Java那样的下标循环;
    #内置的enumerate函数可以把一个list变成索引-元素对
    print i, value