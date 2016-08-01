#coding=utf-8
'''
Created on 2016年3月30日

@author: Administrator
'''
class Student(object):
    
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def set_name(self):
        return self.__name
    def set_score(self):
        return self.__score
    def print_score(self):
        return self.__name, self.__score
        print('%s: %s' %(self.__name, self.__score))
  #  def __str__(self):
  #      return 'The student name and score are (name: %s)' % self.__name
        
class Person(Student):
    
    def get_grade(self):
        if self.get_score() > 90:
            return 'A'
        elif self.get_score()> 80:
            return 'B'
        elif self.get_score() > 60:
            return 'C'
        else:
            return 'D'
       
Person1 = Person('zoe', 65)
Person2 = Person('laura',88)

#print Person1
print Person1.get_grade()
print Person1.print_score()

#import types
#def fn(self, school):
#    self.school = school    
#    pass
#print type(fn) == types.FunctionType

#class Myobj(object):
#    def __init__(self):
#obj = Myobj()
#print hasattr(obj, 'score')
#print getattr(obj, 'name')
#setattr(obj, 'score','A')
#print hasattr(obj, 'score')
#print getattr(obj, 'score')

#s = Student('zoe', 88)
#s.age = '19'
#print s.age

#def set_favoriate(self, favoriate):
#    self.favoriate = favoriate
#s.set_favoriate = types.MethodType(set_favoriate, s)
#print  s.set_favoriate('fruits')
