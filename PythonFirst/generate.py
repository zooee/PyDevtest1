#encoding:utf-8
'''
Created on 2016年3月28日

@author: Administrator
'''
#L = [x * x for x in range(10)]
#print L

#g = (x * x for x in range(10))
#print g
#print g.next()
#for n in g:
#   print n
def fib(max):
    n = 0
    a, b = 0, 1
    while n < max:
        print b
        a, b = b, a + b
        n = n + 1
#print fib(6)

# print abs(-3)
f = abs
print f(-4)

def sum(x, y, f):
    return f(x) * f(y)
print sum(3, -5, abs)

def is_odd(n):
    return n % 2 == 1
L = filter(is_odd, [1,3,2,4,5,6,8])
print L

def not_empty(s):
    return s and s.strip()
L2 = filter(not_empty, ['a', '','b','df',''])
print L2

def primeNum(n):
    for k in range(2, n/2):
        if n % k == 0:
            return 0
    return 1
L3 = filter(primeNum, range(1,101))
print L3
#---------------倒叙
def reversed(x, y):
    if x > y:
        return 1
    if x < y:
        return -1
    return 0
List1 = sorted([34,4,66,246,45,34,23], reversed)
print List1

def sum_add(*args):
    def add():
        a = 0
        for n in args:
            a = a + n
        return a
    return add     #-----返回函数本身
f = sum_add(1,2,3,4,5,6)
print f()   #-----------调用函数f时，才真正计算求和的结果：
#--------------------没看懂
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f1 = count()
print f1
#-----------------------------------------------------
LL = map(lambda x: x * x, [1,2,3,4,5])
print LL

import functools
int2 = functools.partial(int, base = 2)
print int2('64')