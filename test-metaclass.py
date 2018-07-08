#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author: David Pay
#date: 06-20-2018


class Hello(object):
    def hello(self, name='world'):
        print('hello',name)

h = Hello()
h.hello()
print(type(Hello))
print(type(h))
print('--------------------')

def fn(self, name ='world'):
    print("hello",name)

Hello1 = type('Hello1', (object,), dict(tn=fn))

h1 = Hello1()
h1.tn()
print(type(Hello1))
print(type(h1))

print('------------------------------------------------------')

class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs["add"] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class Mylist(list, metaclass=ListMetaclass):
    pass

L = Mylist()
L.add(1)
print(L)
L.add(4)
print(L)

#1 doing this
#2 put add direct in Mylist
#so what is the design pattern here?