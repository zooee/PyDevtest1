#coding=utf-8
'''
Created on 2016年4月1日

@author: Administrator
'''
class Student(object):
    
    @property
    def birth(self):
        return self.__birth
    @birth.setter
    def birth(self, value):
        self.birth = value
    @property
    def age(self):
        return 2016 - self.__birth
    
class Screen(object):
    pass
    @property
    def width(self):
        return self.__width
    @property
    def weight(self):
        return self.__weight
    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise ValueError('width must be an hehehe')
        if width <= 0:
            raise ValueError('width must above 233333')
        self.__width = width
    @weight.setter
    def weight(self, weight):
        self.__weight = weight
    @property
    def resolution(self):
        return self.__width * self.__weight
s = Screen()
s.width = 5
s.weight = 10
print s.resolution
assert s.resolution == 50, '5 * 10 = %d ?' % s.resolution