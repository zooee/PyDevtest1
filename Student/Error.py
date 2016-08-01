#coding=utf-8
'''
Created on 2016年4月5日5

@author: Administrator

'''
a = '1'
try:
    print('try to do ...')
    r = 100/int(a)
    print 'result:', r
except ValueError as e:
    print ('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:',e)
else:
    print 'It ssdfsdfdsf'
finally:
    print 'finally..'
print 'over'