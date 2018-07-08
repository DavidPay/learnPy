#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author: David Pay
#date: 06-19-2018
def powerV1(x):
    return x*x

def powerV2(x, n):
    s = 1
    while n > 0:
        n = n -1
        s = s*x
    return s   

def power(x, n=2):
    s = 1
    while n > 0:
        n = n -1
        s = s*x
    return s

def add_end(L=[]):
    L.append('END')
    return L
    # see Mutable Default Arguments
    # see Late Binding Closures
    # http://docs.python-guide.org/en/latest/writing/gotchas/
    # but when i run debug mode ,i can see from the stack that the L is different each call.
    # and in one print call two add. they are the same

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n *n
    return sum

def person(name, age, **kw):
    print('name:', name, 'age:', age,'other:',kw)
#here even name and age can be **kw

def person1(name, age, *arg, height):
    print(name, age, arg, height)

def person2(name,age,*,height, **kw):
    print(name,age,height,kw)

class PrivateO():
    def __A1(self):
        print("In private A1")
    def B1(self):
        print("call private __A1")
        self.__A1() 
        '''
class argsIn():
    @database.setter
    def database(self, s=""):
        print(s) 
        #name database is not defined
        '''
if __name__ == "__main__":
    print(power(3))
    print(power(3,3))
    print(add_end())
    print(add_end())
    print(add_end(), add_end())
    print(add_end(), add_end(), add_end())
    nums = (1,2,3)
    print(calc(1,2), calc(1,5,4), calc(*nums))
    person("david", 32)
    david1 = {'name':'david', 'age':32, 'height':1.72}
    person(**david1) 
    david2 = {'name':'david', 'age':32, 'weight':100}
    david3 = {'name':'david', 'age':32}
    #person1(**david3) #missing  keyword-only argument
    #person1(**david2) # unexpected keyword argument
    david4 = {'age':32, 'height':1.72, 'weight':100,'name':'david' }
    person2(**david4)


    private1 = PrivateO()
 #   private1.__A1()  
    private1._PrivateO__A1()

    #self should not be self
    '''
    http://www.cnblogs.com/jessonluo/p/4717140.html
    <__main__.Test object at 0x000001E50F2BB860>
    <class '__main__.Test'>
    '''
    class Test:
        def prtNoArgs():
            '''
            class method. 
            called
            as Test.prtNoArgs()
            '''
            print("In prtNoArgs()")
            print('\n')
        def prt(that):
            '''
            called as
            t = Test()
            t.prt() or Test.prt(t)
            '''
            print("In prt(that)")
            print(that)
            print(that.__class__)
            print('\n')

    t = Test()
    Test.prt(t) #
    Test.prtNoArgs()
    class Desc:
        def __get__(self, ins, cls):
            print('self in Desc: %s ' % self )
            print(self, ins, cls)
    class Test2:
        x = Desc()
        def prt(self):
            print('self in Test: %s' % self)
    t2 = Test2()
    t2.prt()
    t2.x