#coding=utf-8
'''
Created on 2016年4月11日

@author: Administrator
'''
'''
try:
    f = open('/Users/Administrator/Desktop/testPy.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()

with open('/Users/Administrator/Desktop/testPy.txt', 'r') as f:
    print (f.read())
'''

from io import StringIO
from io import BytesIO

f1 = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f1.readline()
    if s == '':
        break
    print(s.strip())
#####################################################################
f2 = BytesIO()
f2.write('全世界的我'.encode(encoding='GBK', errors='strict'))
print(f2.getvalue())
######################################################################


'''
#write to BytesIO
f = BytesIO()
f.write(b'hello')
f.write(b' ')
f.write(b'world!')
print (f.getvalue())

#read from BytesIO:
data = '人闲桂花落，夜静春山空。月出惊山鸟，时鸣春涧中。'.encode(encoding='utf_8', errors='strict')
f = BytesIO(data)
print(f.read())

f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())
'''
f = StringIO('水面细风生，\n菱歌慢慢声。\n客亭临小市，\n灯火夜妆明。')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())