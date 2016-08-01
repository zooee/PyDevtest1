#encoding:utf-8
'''
Created on 2016年3月22日

@author: Administrator
'''
import math
#移动xy坐标函数
def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
#求x的n次方函数
def power(x, n = 2):
    s = 1
    while n > 0:
        n = n-1
        s = s * x
    return s
#可变参数*,函数内部可传入一个list或tuple
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum
#函数传入参数类型为list
def add_end(L=[]):
    L.append('end')
    return L
#关键字参数
def per(name, age, **kw):
    print 'name:',name, 'age:',age,'other:',kw
#参数组合
def combination(a,b,c = 0,*args,**kw):
    print 'a=',a, 'b=',b, 'c=',c,'args=',args,'kw=',kw
#空函数
def non():
    pass
#绝对值函数
def myabs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad type')
    if x > 0:
        return x
    else:
        return -x 

#x = int(raw_input("input:" ))
##y = myabs(x)
#print myabs(x)
print myabs(-2)
#print abs('2')
a = move(100, 100, 40, math.pi/6)
print a

print power(2,3)
print add_end([])
print add_end([1,2,3])
print add_end(['a','b','c'])
#函数传入参数类型为list
sum = [1,2,3]
print calc(*sum)
#关键字参数
#print per('Jav', 12, city = 'beijing', gender = 'famale')
kw = {'city': 'beijing', 'job':'engineer'}
print per('zoe',16,**kw)
#组合参数
#print combination(2,3)
#print combination(2,3,33)
#print combination(2,3,33,'a','b', z=2)
args = ['2',2,3,3,3,3]
kw={'x':'xiaoming', 'd':'sjell'}
print combination(4,5,2,*args, **kw)
#递归函数
def fact(n):
    return fact_iter(n, 1)

def fact_iter(n, total):
    if n == 1:
        return total
    return fact_iter(n - 1, n * total)
print fact(5)

L = []
n = 0
#for n in range(100):
while n <= 100:
    L.append(n)
    n = n + 2
print L

T = []
for i in range(100):
    if '3' in str(i):
        T.append(i)
print T