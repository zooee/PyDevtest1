#coding=utf-8
'''
Created on 2016年4月6日

@author: Administrator
'''
import unittest
from __init__ import Dict

class TestDict(unittest.TestCase):
    def test_init(self):
        d = Dict(a = 1, b = 'test')
        self.assertEqual(d.a, 1)    #断言函数返回的结果与1相等
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))
     
    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')
     
    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')
     
    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']   #通过d['empty']访问不存在的key时，断言会抛出KeyError
             
    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty    #通过d.empty访问不存在的key时，我们期待抛出AttributeError   
    #两个方法会分别在每调用一个测试方法的前后分别被执行
    def setUp(self):
        print('setUp..')
        
    def tearDown(self):
        print('tearDown...')
if __name__ == '__main__':   #把myDictTest.py当做正常的python脚本运行
    unittest.main() 
