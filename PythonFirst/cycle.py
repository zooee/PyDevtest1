#encoding:utf-8
'''
Created on 2016年3月17日

@author: Administrator
'''
age = 3

if age >= 18:
    print 'your age is', age
    print 'adult'
elif age >= 6:
    print 'teeneger'
else:
    print 'kids'

range(5)
#循环求1到100的和    
sum = 0
for x in range(101):
    sum = sum + x
print sum
#循环求1到一百的奇数和
sum1 = 0
n = 99
while n > 0:
    sum1 = sum1 + n
    n = n - 2
print sum1
#循环求1到100的偶数和
sum2 = 0
n2 = 100
while n2 > 0:
    sum2 = sum2 + n2
    n2 = n2 - 2
print sum2
#int将输入的字符串转换为数字类型
birth = int(raw_input('birth: '))
if birth < 2000:
    print '00前'
else:
    print '00后'

